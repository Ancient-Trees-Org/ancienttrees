// WHAT THE TREES-IN-VIEW LIST KNOWS (lib/view-list-js.ts), built once for
// /explore and for the city map (Hidde, 2026-11-26: one map on the website).
// /explore writes it into its page as it always did; the city page fetches
// the same thing from /api/map-view/<lang>.json the moment you leave its city,
// so 243 city pages do not each carry every tree. Moved out of
// ExploreMap.astro word for word.
import { getCollection } from "astro:content";
import { cityIsRenderable, renderableTrees, slugify, cityIsOnMap, mapTrees, treeHasPage, feedTreesOf } from "./trees";
import { highlightRanks } from "./highlights";
import { placeHasPage } from "./place-page";
import { ageShort } from "./age-short";
import { SPECIES_ICONS, speciesIconKey } from "./species-icons";
import { speciesCommon, COUNTRY_MIN_CITIES } from "./species";
import { mapSpecies } from "./map-species";
import { cityFace, cityFaceSrcset, usablePhoto } from "./images";
import { miniPin, pinPriority, type ExploreTreeFeature, type ExploreCityRow, type ExploreListData } from "./map";
import { savesOf } from "./saves";
import { placeHasAmbassador } from "./ambassadors";
import { byCityListOrderEntry } from "./city-order";
import { ui, translatedCities, cityTranslation } from "./i18n";

/** A link that stays in the reader's language where a translated page exists,
 * and falls back to English where it does not. */
export function cityHrefFor(lang: string): (slug: string) => string {
  const mine = lang === "en" ? null : new Set(translatedCities(lang));
  return (slug: string) => (mine && mine.has(slug) ? `/${lang}/${slug}` : `/${slug}`);
}

/** A city's name in this language where its overlay gives one. */
export function cityLabelFor(lang: string): (c: { city: string; slug: string }) => string {
  return (c) => (lang !== "en" && cityTranslation(lang, c.slug)?.city) || c.city;
}

export interface ViewListData {
  features: ExploreTreeFeature[];
  cityRows: ExploreCityRow[];
  speciesList: string[];
  speciesLatinHtml: string[];
  listData: ExploreListData;
}

export async function viewListData(lang: string): Promise<ViewListData> {
  const U = ui(lang);
  const cityHref = cityHrefFor(lang);
  const cityLabel = cityLabelFor(lang);
  const allCities = byCityListOrderEntry((await getCollection("cities")).filter(cityIsRenderable));
  const features: ExploreTreeFeature[] = [];
  // The species chip's list, the same on every map (lib/map-species.ts).
  const { list: speciesList, index: speciesIndex, latinHtml: speciesLatinHtml } = await mapSpecies();

  // Every pin, app-only trees included (lib/app-first.ts APP_ONLY_PINS,
  // 2026-11-06): an app-only tree gets no url, so its card opens no page.
  const mapCities = byCityListOrderEntry((await getCollection("cities")).filter(cityIsOnMap));
  // The list under the map (direction B, 2026-11-06): each tree's place in its
  // city's Highlights, the same ranks the app's feed sends (lib/app-feed.ts).
  for (const entry of mapCities) {
    const cslug = entry.id;
    const hlRanks = highlightRanks(cslug, feedTreesOf(entry) as any);
    for (const t of mapTrees(entry)) {
      const short = ageShort(t, U, lang);
      const loc = t.location;
      const sp = speciesIndex.get(speciesCommon(t));
      features.push({
        type: "Feature",
        geometry: { type: "Point", coordinates: [loc.longitude ?? null, loc.latitude ?? null] },
        properties: {
          id: t.id,
          name: t.name,
          url: treeHasPage(t) ? `${cslug}/${slugify(t.name)}` : "",
          cs: cslug,
          city: entry.data.city,
          age: t.age_estimate ?? "",
          now: 0 as 0 | 1,
          pr: pinPriority(Boolean(usablePhoto(t)), savesOf(t.id)),
          mn: (miniPin(t.id, Boolean(usablePhoto(t))) ? 1 : 0) as 0 | 1,
          ...(t.paid_entry ? { paid: 1 as 1 } : {}),
          ...(sp === undefined ? {} : { sp }),
          ...(hlRanks.has(t.id) ? { hl: hlRanks.get(t.id)! } : {}),
          ...(short ? { as: short } : {}),
        },
      });
    }
  }

  // The panel's city cards need a face and a rank: hero photo per the Cadiz
  // standard where set, favourites first (the homepage list), then tree
  // count. No counts in the page copy itself (Hidde, 2026-07-29): "je moet
  // nadenken dat alles wat je maakt ooit gaat bestaan uit miljoenen bomen."
  const FAVES = ["lisbon", "cadiz", "porto", "amsterdam", "kyoto", "rome", "palermo", "paris", "london", "barcelona"];
  const cityRows: ExploreCityRow[] = allCities
    .filter((e) => renderableTrees(e).length > 0)
    .map((e) => {
      const trees = renderableTrees(e);
      return {
        city: e.data.city,
        url: e.id,
        country: e.data.country,
        n: trees.length,
        lat: trees.reduce((s, t) => s + (t.location.latitude ?? 0), 0) / trees.length,
        lng: trees.reduce((s, t) => s + (t.location.longitude ?? 0), 0) / trees.length,
        ph: cityFace(e.data, 172),
        ph2: cityFaceSrcset(e.data, 86)?.srcset ?? null,
        rank: FAVES.includes(e.id) ? FAVES.indexOf(e.id) : 99,
      };
    })
    .sort((a, b) => a.rank - b.rank || b.n - a.n);

  // The list's places: every city on the map with its name in this language,
  // its country, and its page where it has one (a place with one tree on the web
  // has none, lib/place-page.ts); every country with a page (Contract G, the
  // rule [country].astro builds by). Country pages are English only.
  const listData: ExploreListData = { places: {}, countries: {}, icons: SPECIES_ICONS,
    speciesIcon: speciesList.map((s) => speciesIconKey(s)) };
  for (const e of mapCities) {
    const web = cityIsRenderable(e) ? renderableTrees(e).length : 0;
    listData.places[e.id] = {
      n: cityLabel({ city: e.data.city, slug: e.id }),
      k: e.data.country,
      h: web > 0 && placeHasPage(e.id, web) ? cityHref(e.id) : "",
      ...(placeHasAmbassador(e.id) ? { a: 1 } : {}),
    };
  }
  const citiesPerCountry = new Map<string, number>();
  for (const e of allCities) citiesPerCountry.set(e.data.country, (citiesPerCountry.get(e.data.country) ?? 0) + 1);
  for (const intro of await getCollection("countries")) {
    if ((citiesPerCountry.get(intro.data.country) ?? 0) >= COUNTRY_MIN_CITIES) {
      listData.countries[intro.data.country] = `/${intro.data.slug}`;
    }
    // The place head's intro for a searched country: the country page's own
    // words, on the English map only (the overlays carry no country intros).
    if (lang === "en" && intro.data.intro) (listData.intros ??= {})[intro.data.country] = intro.data.intro;
  }
  return { features, cityRows, speciesList, speciesLatinHtml, listData };
}
