// What the trees-in-view list knows, for the city map (Hidde, 2026-11-26:
// one map on the website). /explore writes the same into its own page; a city
// page fetches this file only once you leave its city, when its panel becomes
// the map's trees in view (lib/view-list-js.ts). One file per language, since
// the list's words, place names and short ages are in the page's language.
import { viewListData } from "../../../lib/view-list-data";
import { viewListWords } from "../../../lib/view-list-js";
import { EXPLORE_LIST_MAX } from "../../../lib/map";
import { translatedLanguages } from "../../../lib/i18n";

export function getStaticPaths() {
  return ["en", ...translatedLanguages()].map((lang) => ({ params: { lang } }));
}

export async function GET({ params }: { params: { lang: string } }) {
  const lang = params.lang;
  const { features, speciesList, speciesLatinHtml, listData } = await viewListData(lang);
  const w = viewListWords(lang);
  const body = {
    features,
    species: speciesList,
    speciesLatin: speciesLatinHtml,
    places: listData.places,
    countries: listData.countries,
    intros: listData.intros || {},
    icons: listData.icons,
    speciesIcon: listData.speciesIcon,
    words: w.words,
    empty: w.empty,
    chevron: w.chevron,
    boxIc: w.boxIc,
    listMax: EXPLORE_LIST_MAX,
  };
  return new Response(JSON.stringify(body), { headers: { "Content-Type": "application/json" } });
}
