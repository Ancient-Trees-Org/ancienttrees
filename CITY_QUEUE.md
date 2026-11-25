# CITY_QUEUE: the one list, the one order, and how far to take a city

Written 2026-08-11 because Hidde said what everyone could see: "there are
multiple city prioritisations living amongst each other". There were six, and
they disagreed. This file replaces all of them. If another document names a
city order, it is stale and this one wins.

## The rule, derived from our own numbers rather than chosen

**Rewritten 2026-08-15, and it replaces the fame-penalty rule this file was
founded on.** Hidde asked whether Wikipedia pageviews really represent an
English-speaking tourist. They do not, and testing that question properly took
the old rule down with it. Both halves of the score were checked against the
one outcome we care about, `impressions_10d` from the Search Console readback,
on the 55 published cities Google has actually indexed:

| proxy | rank correlation with our impressions |
|---|---:|
| English Wikipedia pageviews (the old demand term) | +0.23 |
| **English Wikivoyage pageviews** (the new one) | **+0.33** |
| English share of pageviews (the anglophone idea) | +0.11 |

**Demand is travel intent, not fame.** `travel` (English Wikivoyage pageviews,
`scripts/travel_demand.py`) is the size term. Someone reading a Wikivoyage
article is planning a trip; someone reading Wikipedia is settling an argument.
Potsdam is famous for a conference and nobody packs a bag for it, which is
exactly the city the old proxy sent us to.

**The fame penalty is gone, and this file was wrong about it.** The founding
claim was "the more famous a city is, the worse we do there", drawn from ten
cities in a digest, and it paid out as a band multiplying contested cities by
1.08 and quiet ones by 2.50. On all 111 published cities it does not survive.
Split by travel demand into thirds:

| travel demand | cities | impressions per 100k travel views | clicks |
|---|---:|---:|---:|
| low | 37 | 206 | 12 |
| middle | 37 | 224 | 23 |
| high | 37 | 184 | 33 |

Impressions are flat and clicks run the other way outright. So the predicted
yield is now **flat**: we stopped penalising fame and deliberately did not
start rewarding it, because those click counts are small and half the site is
still unindexed. The old ten-city table was not a lie, it was a sample.

**The anglophone hypothesis was tested and failed**, and is recorded here so it
is not proposed again. Ranking by how English-dominant a city's readership is
scores +0.11, which is nothing, and our six best pages (Palermo, Amsterdam,
Rome, Prague, Barcelona, Vienna) are all in countries that read about
themselves in their own language. Measured on published pages, anglophone
cities earn 1.33 impressions per tree against 1.43 everywhere else: a wash.
English speakers do not read in English about where they live, they TRAVEL to
continental Europe, and Wikivoyage catches that while a language ratio cannot.

So the score is **travel demand times realised yield**, and yield comes from
evidence in this order:

1. **Measured**, where Search Console has spoken: what the city actually earns
   per 1,000 travel views, normalised so the median measured city sits at 1.0.
   53 cities.
2. **Published and never ranked** scores 0.25. This is now the shakiest rule
   here rather than the firmest, and it should be read with suspicion: it was
   written when a live page taking no clicks read as evidence of no demand, and
   we have since learned that 346 pages sit "Discovered - currently not
   indexed". London, Edinburgh, Portland, Hobart and Quebec City all show zero
   while never having been crawled, which is evidence of no crawl, not of low
   yield. Kept because demoting a page we cannot see is still the safer error;
   revisit the moment indexing improves.
3. **Predicted** for unpublished places: flat, at travel demand times 1.0.

`ease` is unchanged and still multiplies the order of work: a city with a
register nearby is cheap to open, measured at 0.4k tokens per tree against 27k
for research from zero.

## How far to take a city, and when to stop

The floor is unchanged: four verified trees or no page.

**Settled 2026-08-19, after two corrections the same morning.** Both are Hidde's
and the second overrides the first, so read them in order.

1. **OPEN THE UNOPENED CITIES FIRST.** He said it after looking at the list
   itself: "persoonlijk denk ik dat deze steden zonder register toch starten
   interessanter is dan verdiepen... deze zsm naar 10 krijgen." He named
   Seattle, Dallas, Houston, Cologne, Perth, Sydney, Las Vegas, Frankfurt,
   Bilbao, Dubai, Kansas City, Mexico City, Vancouver, Manchester, Taipei,
   Buenos Aires and Hawaii: all ranked, all at zero trees, most with no
   register behind them. The reasoning is in the numbers he was reading. A new
   city taken to 10 is a page that can start ranking; a thirtieth tree in Rome
   is marginal.

   **This means from-zero web research is ON for these**, which is normally off.
   Rule one (d) has always allowed it when Hidde names the city, and he has.
   Expect them to cost web-research rates rather than register rates, and use
   the 80/20 rule hard: a city that will not give up four good trees cheaply is
   not a city to grind on.

2. **Then deepen, to these targets.** Superseded again on 2026-09-23: Hidde
   said "kijk naar hoe groot een stad is en stel daar het plafond op, ik denk
   dat het zo simpel is", and it is. The ceiling is population, not whether
   Search Console has confirmed the city yet; confirmation now only moves the
   queue's *order* (via `score`), never the *ceiling*. `target_for()` in
   scripts/city_queue.py is the one place this number is computed:

   | population | target |
   |---|---:|
   | under 50,000 | 10 |
   | 50,000 to 250,000 | 20 |
   | 250,000 to 1m | 30 |
   | 1m to 5m | 60 |
   | over 5m | 100 |

   His three calibration points: Baarn (24,528) stops at 10, Copenhagen
   (602,481) at 30, Tokyo (14,047,594) at 100. A city whose population could
   not be resolved keeps the prior behaviour rather than silently dropping to
   10. This retires the prior state-keyed table (new/unconfirmed -> 10,
   confirmed -> 20, confirmed BIG -> 30), which read a big city that Search
   Console had not yet confirmed as capped at 10: that conflated two
   different questions, how many trees a place could hold and where the next
   hour of work goes, and only the second should key off measured demand.

3. **The 80/20 rule governs everything above** (his words: "eeuwig tokens
   gebruiken tot deze max te halen is niet de strategie... als het er wat
   minder zijn maar het wordt te moeilijk om de volgende te vinden ga gewoon
   door"). A target is a ceiling and a stopping point, never a quota. Cadiz at
   5 is finished work.

4. **The queue re-ranks itself daily** from the digest's Search Console
   readback, so a city that starts performing climbs on its own.

What the target is NOT, unchanged: never a quota, never a floor, and the bar
per tree never moves. A city above its target (Barcelona at 46) is finished,
with nothing ever removed. Padding stays forbidden. Nothing here re-opens
whether a tree may be published: only the hard rules and an unstatable location
stop that (2026-08-10).

**Superseded on the way here, kept because the mistakes instruct:** the
supply-banded 20/30/50 of 2026-08-12 (killed with "maar waarom in godsnaam 50
doel bij wenen": a register measures how EASY trees are to find, never how GOOD
they are), a flat 25 for everyone (same day), and 10-then-25-on-confirmation
(same evening, refined into the staircase above). "A city is finished at three
walks" survives only as what the PAGE leads with: readers get the best three
walks, everything else stays published, on the map, collectible, listed below.

Deep enough, per Hidde 2026-08-08, unchanged: at least one complete walk of 4
to 8 trees inside roughly 2 km, photographs on most of that walk, honest pins
(labelled honestly, NOT confirmed), season data where it is real.

## The order

Work top-down. Reader submissions and a broken site still outrank everything.

**The pool is Western tourism, the order is three factors multiplied** (Hidde,
2026-08-13: "een top 250 gebaseerd op westers toerisme... potentie qua toerisme
+ bewezen google prestatie + gemak in opstellen"). Candidates enter the list for
being places Western tourists actually go; each carries measured demand
(**English Wikivoyage pageviews since 2026-08-15**, fetched per city, never
guessed; the Wikipedia figure it replaced is kept in the `demand` column for
comparison and is no longer what the rank is built on). The rank multiplies score
(demand times realised yield, clicks once measured) by an ease factor of 1.0 to
2.0: half for a country whose register story is proven (Portugal, Italy, Japan,
Ireland, Spain, the Dutch municipal pattern), half for register supply already
imported near the city. The boundary that keeps ease honest, from the Vienna-50
mistake of 2026-08-12: **ease multiplies the order of work, never the target.**
A register says cheap, not good.

**The pool was audited and widened on 2026-08-17, in two ways, both on Hidde's questions.**

**First, cities that were simply never in it.** He asked whether we were missing American cities, and we were: 15 in a 293-city list, while the United States is our largest English-speaking source of visitors. Then he asked whether there were more, and there were. The audit was done against the most-read English WIKIVOYAGE articles of the last three months, 1,684 of them, diffed against this list, because that is the same metric the score already uses and it does not depend on anyone remembering a city. **41 places were added**: eleven American (Las Vegas enters at rank 22, above New York; Dallas and Houston in the forties), six Canadian (Halifax at 10,562 travel demand), three Finnish, two Australian, and the islands below. The cause of the gap is worth naming so it does not return: the pool was originally assembled by hand around European city-break tourism, so places that are not city breaks (Dallas, Houston, Kansas City, Winnipeg) never entered it. The audit is repeatable and should be re-run when the list feels stale; the method's one limit is that Wikivoyage's top list is truncated, so it finds the big holes and not the tail.

**Second, ISLANDS are now in the pool, and they are ranked by a rule that travel demand alone gets wrong** (Hidde, 2026-08-17: "ook kan ik me voorstellen dat eilanden interessant zijn en mss verdienen die een andere aanpak"). Seventeen entered, carrying `kind: "island"`. On travel demand they look mediocre, Santorini highest at 9,628 and Yakushima at 1,134, which would put most of them past rank 100. Two things the number cannot see argue the other way. **Competition is close to zero**: nobody writes in English about the old trees of La Gomera, and thin competition is where this site actually ranks. And **the product fit is better than any city's**: on a city page we compete with museums and restaurants for a visitor's afternoon, while on an island where people came to walk, we are the thing they came for. The trees carry the rest of the argument, since these are destinations in themselves: Yakushima's Jomon Sugi (UNESCO, thousands of years old), Tenerife's Drago Milenario, Sicily's Hundred Horse Chestnut, the laurel forests of La Gomera and Madeira that survived the Tertiary.

What this does NOT change: an island enters as an ordinary place in this one list and ships under the existing contracts. Nothing here creates a new page type, which would need Hidde's yes under hard rule 7. The schema already allows it, because it is keyed on coordinates rather than on the word city, which was the point of the third goal.

**The pool narrowed on 2026-08-15: high-income destinations only, for now.**
Hidde, in two messages minutes apart: "Let's keep India out of the top 250 for
now. It's a huge country I don't want to focus on now", then "I want to focus on
cities for rich tourists." The rule is about the country VISITED rather than the
wealth of the visitor, and his own India cut is what settles that: Agra and
Jaipur are visited by affluent Westerners in large numbers and he cut them
anyway. Implemented in `scripts/rescore.py` on the World Bank income
classification, because it is a published citable line rather than a list
somebody felt good about: high income full weight, upper-middle half weight
(Thailand, Mexico, Brazil, Turkey, South Africa and the Balkans survive,
halved), low and lower-middle **paused**. Nineteen unpublished cities left the
list, the biggest being Ho Chi Minh City, Marrakech, Delhi, Ubud and Siem Reap.
Paused is not deleted: the row, its travel demand and its register supply all
stay, a published city is never unranked this way (hard rule 3), and lifting it
is deleting a line from one table. **A run may not add or remove a country
there.** The cost is real and is not hidden: several paused cities are places
the product would serve well, and this is a focus decision rather than a verdict
on them.

**The source is `data/city-queue.json`, not this table.** Hidde asked for one
source file carrying the priority of the 100 cities and the tree target per city
(2026-08-12), and this is the rendering of it. Everything measurable in the row
(trees, photos, walks, register, target) is recomputed by
`python3 scripts/city_queue.py` and written into the json first; `score`,
`demand` and `basis` are the session-decided columns and live there too.
`data/city-list.json` is generated from the same source as the inventory the
site and scripts read. Editing a row here by hand makes a second source again,
so qa.py fails the deploy when the table and the json disagree.

| # | city | score | demand | trees | photos | walks | register | target | basis |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Monterey | 211.33 | - | 3 | 2 | - | - | 10 | measured |
| 2 | Tenerife | 57.64 | - | 9 | 6 | - | - | 30 | measured |
| 3 | London | 72.05 | 718,291 | 55 | 48 | 2 | - | 100 | measured |
| 4 | Malaga | 48.03 | 117,780 | 10 | 5 | 1 | - | 30 | measured |
| 5 | Paris | 28.82 | 524,268 | 60 | 17 | 8 | 129 | 60 | measured |
| 6 | Lisbon | 19.21 | 201,877 | 38 | 23 | 3 | 67 | 30 | measured |
| 7 | Rome | 19.21 | 358,876 | 32 | 13 | 2 | 31 | 60 | measured |
| 8 | Kyoto | 19.21 | 142,353 | 19 | 16 | 2 | - | 60 | measured |
| 9 | Los Angeles | 28.82 | 665,559 | 20 | 6 | 1 | - | 60 | measured |
| 10 | Madrid | 14.41 | 274,553 | 18 | 11 | 2 | - | 60 | measured |
| 11 | Seville | 14.41 | 170,545 | 44 | 12 | 2 | - | 30 | measured |
| 12 | Lyon | 14.41 | 136,951 | 34 | 6 | 6 | 178 | 30 | measured |
| 13 | Long Beach | 20.48 | - | - | - | - | - | 30 | predicted (travel demand) |
| 14 | Little Rock | 20.40 | - | - | - | - | - | 20 | predicted (travel demand) |
| 15 | Seattle | 19.21 | 398,724 | 30 | 3 | 4 | - | 30 | measured |
| 16 | Charleston | 19.21 | 155,987 | 4 | 1 | - | - | 20 | measured |
| 17 | Barcelona | 9.61 | 346,477 | 59 | 21 | 7 | 180 | 60 | measured |
| 18 | Enschede | 9.61 | - | 13 | 1 | 1 | 82 | 20 | measured |
| 19 | Palermo | 9.61 | 124,310 | 27 | 14 | 3 | 38 | 30 | measured |
| 20 | Cambridge | 19.21 | 97,974 | 11 | 3 | 1 | - | 20 | measured |
| 21 | Montreal | 19.21 | 315,322 | 14 | 2 | 2 | - | 60 | measured |
| 22 | Reno | 18.19 | - | - | - | - | - | 30 | predicted (travel demand) |
| 23 | Des Moines | 18.11 | - | - | - | - | - | 20 | predicted (travel demand) |
| 24 | Daytona Beach | 17.66 | - | - | - | - | - | 20 | predicted (travel demand) |
| 25 | Dublin | 9.61 | 240,850 | 20 | 5 | 2 | 12 | 30 | measured |
| 26 | Girona | 9.61 | 51,072 | 7 | 3 | - | - | 20 | measured |
| 27 | Huntsville | 15.35 | - | - | - | - | - | 20 | predicted (travel demand) |
| 28 | Saratoga Springs | 15.05 | - | - | - | - | - | 10 | predicted (travel demand) |
| 29 | West Palm Beach | 14.98 | - | - | - | - | - | 20 | predicted (travel demand) |
| 30 | Saint Petersburg | 14.83 | - | - | - | - | - | 100 | predicted (travel demand) |
| 31 | Edinburgh | 14.41 | 292,981 | 22 | 12 | 1 | - | 30 | measured |
| 32 | Antwerp | 14.41 | 128,289 | 10 | 5 | 1 | - | 30 | measured |
| 33 | Berlin | 9.61 | 412,181 | 63 | 51 | 5 | 195 | 60 | measured |
| 34 | Munich | 9.61 | 224,067 | 63 | 36 | 8 | 74 | 60 | measured |
| 35 | Detroit | 12.53 | - | - | - | - | - | 30 | predicted (travel demand) |
| 36 | Jerusalem | 11.17 | 314,788 | - | - | - | - | 60 | predicted (travel demand) |
| 37 | Dubai | 11.02 | 334,167 | - | - | - | - | 60 | predicted (travel demand) |
| 38 | Oslo | 9.61 | 181,113 | 6 | 5 | 1 | - | 30 | measured |
| 39 | New York | 9.61 | 1,124,326 | 99 | 13 | 8 | - | 100 | measured |
| 40 | Jersey City | 10.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 41 | Anchorage | 10.25 | - | - | - | - | - | 30 | predicted (travel demand) |
| 42 | Raleigh | 10.07 | - | - | - | - | - | 30 | predicted (travel demand) |
| 43 | Copenhagen | 9.61 | 218,621 | 53 | 48 | 7 | - | 30 | measured |
| 44 | El Paso | 9.70 | - | - | - | - | - | 30 | predicted (travel demand) |
| 45 | Las Vegas | 9.64 | - | 13 | 6 | 2 | - | 30 | published, never ranked (may be uncrawled) |
| 46 | Santorini | 9.63 | - | - | - | - | - | 10 | predicted (travel demand) |
| 47 | Austin | 9.61 | 226,631 | 12 | 5 | 1 | - | 30 | measured |
| 48 | Minneapolis | 9.61 | - | 4 | - | - | - | 30 | measured |
| 49 | Alicante | 4.80 | 77,454 | 21 | 4 | 2 | 44 | 30 | measured |
| 50 | Deventer | 4.80 | - | 12 | - | 1 | 213 | 20 | measured |
| 51 | Milan | 4.80 | 212,705 | 30 | 14 | 3 | 25 | 60 | measured |
| 52 | Porto | 4.80 | 120,415 | 32 | 16 | 3 | 40 | 30 | measured |
| 53 | Sintra | 4.80 | 46,889 | 8 | 6 | 1 | 6 | 30 | measured |
| 54 | Utrecht | 4.80 | 67,963 | 30 | 9 | 2 | 339 | 30 | measured |
| 55 | Venlo | 4.80 | - | 7 | - | 1 | 144 | 20 | measured |
| 56 | Amsterdam | 4.79 | 294,030 | 28 | 11 | 2 | 5488 | 30 | published, never ranked (may be uncrawled) |
| 57 | Birmingham | 9.38 | - | 1 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 58 | Edmonton | 9.38 | - | - | - | - | - | 60 | predicted (travel demand) |
| 59 | Winnipeg | 9.21 | - | - | - | - | - | 30 | predicted (travel demand) |
| 60 | Bologna | 4.80 | 146,161 | 14 | 9 | 1 | 9 | 30 | measured |
| 61 | Tampere | 8.78 | - | - | - | - | - | 30 | predicted (travel demand) |
| 62 | Genoa | 4.80 | 145,206 | 13 | 2 | 1 | 10 | 30 | measured |
| 63 | Tokyo | 4.80 | 394,702 | 24 | 18 | 1 | 6 | 100 | measured |
| 64 | Venice | 4.80 | 267,527 | 12 | 7 | 2 | 4 | 30 | measured |
| 65 | Luang Prabang | 7.49 | 24,534 | - | - | - | - | 20 | predicted (travel demand) |
| 66 | Mexico City | 7.20 | 566,583 | 10 | 3 | - | - | 100 | measured |
| 67 | Fukuoka | 4.80 | 77,485 | 19 | 12 | 1 | - | 60 | measured |
| 68 | Bergen | 7.30 | 82,940 | - | - | - | - | 30 | predicted (travel demand) |
| 69 | Frankfurt | 4.80 | 150,379 | 28 | 13 | 1 | - | 30 | measured |
| 70 | Leipzig | 4.80 | 121,319 | 31 | 24 | 4 | - | 30 | measured |
| 71 | Melbourne | 4.80 | 267,898 | 21 | 9 | 3 | 389 | 100 | measured |
| 72 | Ottawa | 4.80 | - | 26 | 1 | 3 | 120 | 60 | measured |
| 73 | Prague | 4.80 | 303,350 | 30 | 21 | 4 | 31 | 60 | measured |
| 74 | Singapore | 4.80 | 967,821 | 34 | 7 | 3 | 165 | 100 | measured |
| 75 | Vilnius | 4.80 | 113,188 | 12 | 4 | 1 | 34 | 30 | measured |
| 76 | Gyeongju | 6.94 | 30,260 | - | - | - | - | 20 | predicted (travel demand) |
| 77 | Siena | 4.62 | 57,436 | - | - | - | - | 20 | predicted (travel demand) |
| 78 | Santiago de Compostela | 4.52 | 93,477 | - | - | - | - | 20 | predicted (travel demand) |
| 79 | Zagreb | 6.42 | 122,890 | - | - | - | - | 30 | predicted (travel demand) |
| 80 | Bogota | 6.39 | 1,623 | - | - | - | - | 100 | predicted (travel demand) |
| 81 | Funchal | 3.77 | 174,351 | - | - | - | - | 20 | predicted (travel demand) |
| 82 | Hawaii | 6.19 | - | 8 | - | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 83 | Dallas | 6.15 | - | 12 | 2 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 84 | Houston | 6.11 | - | 12 | 2 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 85 | Toronto | 5.96 | 411,011 | 7 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 86 | San Francisco | 4.04 | 361,111 | 12 | 3 | 1 | 26 | 30 | published, never ranked (may be uncrawled) |
| 87 | Vienna | 3.87 | 283,090 | 61 | 26 | 6 | 358 | 60 | published, never ranked (may be uncrawled) |
| 88 | Alice Springs | 5.71 | - | - | - | - | - | 10 | predicted (travel demand) |
| 89 | Jacksonville | 5.69 | - | 2 | 2 | - | - | 30 | published, never ranked (may be uncrawled) |
| 90 | Chicago | 5.14 | 485,769 | 55 | 2 | 6 | 5 | 60 | published, never ranked (may be uncrawled) |
| 91 | Avignon | 5.54 | 64,047 | - | - | - | - | 20 | predicted (travel demand) |
| 92 | Galway | 3.65 | 88,162 | - | - | - | - | 20 | predicted (travel demand) |
| 93 | Phuket | 5.46 | 5,487 | - | - | - | - | 30 | predicted (travel demand) |
| 94 | Spokane | 3.92 | - | 18 | - | 2 | 18 | 20 | published, never ranked (may be uncrawled) |
| 95 | Rovaniemi | 5.38 | - | - | - | - | - | 20 | predicted (travel demand) |
| 96 | Aarhus | 5.23 | 52,722 | 7 | 1 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 97 | Lagos | 3.43 | 34,452 | - | - | - | - | 100 | predicted (travel demand) |
| 98 | Kansas City | 5.26 | - | 5 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 99 | Asheville | 5.22 | - | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 100 | Seoul | 4.80 | 206,265 | 8 | 5 | 1 | - | 100 | measured |
| 101 | Lund | 5.14 | - | - | - | - | - | 20 | predicted (travel demand) |
| 102 | Kobe | 3.40 | 54,798 | - | - | - | - | 60 | predicted (travel demand) |
| 103 | Hamburg | 4.80 | 191,221 | 6 | 5 | 1 | - | 60 | measured |
| 104 | Boise | 5.07 | - | 4 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 105 | Sydney | 4.92 | 305,304 | 9 | 5 | - | - | 100 | published, never ranked (may be uncrawled) |
| 106 | Budapest | 4.80 | 283,807 | 13 | 2 | 3 | - | 60 | measured |
| 107 | Heraklion | 4.96 | 66,359 | - | - | - | - | 20 | predicted (travel demand) |
| 108 | Marseille | 4.96 | 182,033 | - | - | - | - | 30 | predicted (travel demand) |
| 109 | Oxford | 4.80 | 111,583 | 8 | 3 | 1 | - | 20 | measured |
| 110 | Fort Lauderdale | 4.61 | - | 16 | - | - | 2 | 20 | published, never ranked (may be uncrawled) |
| 111 | Manchester | 4.80 | 316,438 | 5 | 1 | - | - | 30 | measured |
| 112 | Brisbane | 3.18 | 162,602 | 21 | 6 | 2 | 186 | 60 | published, never ranked (may be uncrawled) |
| 113 | Lexington | 4.56 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 114 | Ho Chi Minh City | 4.70 | 193,859 | 1 | - | - | - | 100 | published, never ranked (may be uncrawled) |
| 115 | Oakland | 4.70 | - | 4 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 116 | Basel | 4.59 | 105,838 | - | - | - | - | 20 | predicted (travel demand) |
| 117 | Portland | 3.06 | 217,222 | 33 | 2 | 3 | 306 | 30 | published, never ranked (may be uncrawled) |
| 118 | Indianapolis | 4.57 | - | 5 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 119 | Key West | 3.95 | - | 8 | 5 | 1 | 7 | 10 | published, never ranked (may be uncrawled) |
| 120 | Boston | 4.28 | 385,902 | 40 | 6 | 4 | - | 30 | published, never ranked (may be uncrawled) |
| 121 | Florence | 2.21 | 184,099 | 29 | 9 | 1 | 27 | 30 | published, never ranked (may be uncrawled) |
| 122 | Valencia | 2.21 | 162,209 | 31 | 4 | 2 | 350 | 30 | published, never ranked (may be uncrawled) |
| 123 | Tasmania | 4.41 | - | - | - | - | - | 30 | predicted (travel demand) |
| 124 | Glasgow | 4.29 | 253,705 | 10 | 6 | - | - | 30 | published, never ranked (may be uncrawled) |
| 125 | Ravenna | 2.77 | 86,471 | - | - | - | 1 | 20 | predicted (travel demand) |
| 126 | Sofia | 2.81 | 138,710 | 4 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 127 | San Sebastian | 2.80 | 367 | - | - | - | - | 20 | predicted (travel demand) |
| 128 | Perth | 4.10 | 180,478 | 6 | 4 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 129 | Chattanooga | 4.17 | - | 2 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 130 | Tel Aviv | 4.09 | 177,885 | - | - | - | - | 30 | predicted (travel demand) |
| 131 | Interlaken | 4.06 | 24,936 | - | - | - | - | 10 | predicted (travel demand) |
| 132 | Brussels | 2.70 | 176,863 | 36 | 12 | 3 | 436 | 60 | published, never ranked (may be uncrawled) |
| 133 | Washington DC | 3.68 | 606,731 | 35 | 9 | 4 | - | 30 | published, never ranked (may be uncrawled) |
| 134 | Santa Cruz | 4.01 | - | 2 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 135 | Eindhoven | 1.99 | - | 17 | - | 3 | 195 | 20 | published, never ranked (may be uncrawled) |
| 136 | Osaka | 2.54 | 163,112 | 6 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 137 | Pittsburgh | 3.80 | - | 12 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 138 | Salt Lake City | 2.58 | - | 20 | 4 | 2 | 29 | 20 | published, never ranked (may be uncrawled) |
| 139 | Taormina | 2.35 | 33,169 | - | - | - | 5 | 10 | predicted (travel demand) |
| 140 | Niagara Falls | 3.68 | - | - | - | - | - | 20 | predicted (travel demand) |
| 141 | Kuala Lumpur | 3.80 | 191,800 | - | - | - | - | 100 | predicted (travel demand) |
| 142 | Bratislava | 2.49 | 132,162 | 7 | 1 | 1 | 26 | 30 | published, never ranked (may be uncrawled) |
| 143 | St. Louis | 3.70 | - | 6 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 144 | Strasbourg | 2.45 | 154,700 | 10 | 2 | 2 | 66 | 30 | published, never ranked (may be uncrawled) |
| 145 | Kauai | 3.67 | - | 9 | 2 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 146 | Wellington | 3.60 | 132,267 | - | - | - | - | 20 | predicted (travel demand) |
| 147 | Naples | 1.83 | 198,913 | 32 | 6 | 3 | 47 | 30 | published, never ranked (may be uncrawled) |
| 148 | Bangkok | 3.32 | 222,206 | 6 | 1 | 1 | 5 | 100 | published, never ranked (may be uncrawled) |
| 149 | Bari | 2.16 | 86,456 | 5 | 1 | - | 8 | 30 | published, never ranked (may be uncrawled) |
| 150 | Rotterdam | 1.81 | 104,938 | 17 | 1 | 2 | 83 | 30 | published, never ranked (may be uncrawled) |
| 151 | Hong Kong | 2.40 | 689,212 | 21 | 6 | 2 | 505 | 100 | measured |
| 152 | Warsaw | 2.40 | 197,929 | 39 | 21 | 4 | 1407 | 60 | published, never ranked (may be uncrawled) |
| 153 | Tampa | 3.52 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 154 | Stockholm | 2.82 | 188,184 | 8 | 7 | - | - | 30 | published, never ranked (may be uncrawled) |
| 155 | Montpellier | 3.47 | 64,238 | - | - | - | - | 30 | predicted (travel demand) |
| 156 | Canberra | 2.28 | - | 8 | 2 | 1 | 132 | 30 | published, never ranked (may be uncrawled) |
| 157 | Rhodes | 3.42 | 127,205 | - | - | - | - | 20 | predicted (travel demand) |
| 158 | Cincinnati | 3.33 | - | 8 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 159 | San Antonio | 3.32 | - | 5 | 1 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 160 | Chania | 3.30 | 47,379 | - | - | - | - | 20 | predicted (travel demand) |
| 161 | Fort Worth | 3.28 | - | 29 | - | 2 | - | 30 | published, never ranked (may be uncrawled) |
| 162 | Hilo | 3.27 | - | 9 | - | 2 | - | 10 | published, never ranked (may be uncrawled) |
| 163 | Delhi | 3.26 | 225,133 | 2 | 2 | - | - | 10 | published, never ranked (may be uncrawled) |
| 164 | Lansing | 3.25 | - | 2 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 165 | Santiago | 3.25 | 111,647 | - | - | - | - | 100 | predicted (travel demand) |
| 166 | Sarajevo | 3.15 | 205,074 | - | - | - | - | 30 | predicted (travel demand) |
| 167 | Krakow | 2.09 | 140,824 | 38 | 11 | 3 | 198 | 30 | published, never ranked (may be uncrawled) |
| 168 | Lucerne | 3.10 | 66,356 | - | - | - | - | 20 | predicted (travel demand) |
| 169 | Miami | 2.37 | 278,558 | 19 | 1 | 2 | 15 | 30 | published, never ranked (may be uncrawled) |
| 170 | Malmo | 3.07 | 103,940 | - | - | - | - | 30 | predicted (travel demand) |
| 171 | Lille | 3.06 | 73,435 | - | - | - | - | 20 | predicted (travel demand) |
| 172 | Cologne | 3.04 | 191,812 | 5 | - | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 173 | Ljubljana | 2.98 | 125,046 | 4 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 174 | Tulsa | 3.01 | - | 2 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 175 | Corsica | 3.00 | - | - | - | - | - | 30 | predicted (travel demand) |
| 176 | Mechelen | 2.93 | 20,707 | - | - | - | - | 20 | predicted (travel demand) |
| 177 | The Hague | 1.49 | 236,723 | 26 | 4 | 5 | 166 | 30 | published, never ranked (may be uncrawled) |
| 178 | Turin | 1.49 | 147,456 | 12 | 11 | 2 | 30 | 30 | published, never ranked (may be uncrawled) |
| 179 | Chiang Mai | 2.85 | 66,541 | 3 | 2 | - | 2 | 60 | published, never ranked (may be uncrawled) |
| 180 | Denver | 2.91 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 181 | Nuremberg | 1.94 | 161,614 | 20 | 8 | 2 | 37 | 30 | published, never ranked (may be uncrawled) |
| 182 | Bilbao | 1.93 | 133,133 | 4 | 4 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 183 | Philadelphia | 2.67 | 405,294 | 14 | 5 | - | - | 60 | published, never ranked (may be uncrawled) |
| 184 | Trieste | 1.43 | 117,233 | 36 | 1 | 3 | 43 | 20 | published, never ranked (may be uncrawled) |
| 185 | San Jose | 2.85 | - | 2 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 186 | Groningen | 1.42 | 31,401 | 17 | 5 | 2 | 76 | 20 | published, never ranked (may be uncrawled) |
| 187 | Helsinki | 2.25 | 148,908 | 12 | 3 | 1 | 13 | 30 | published, never ranked (may be uncrawled) |
| 188 | Poznan | 1.89 | 65,666 | 10 | - | 1 | 397 | 30 | published, never ranked (may be uncrawled) |
| 189 | Sacramento | 2.83 | - | 2 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 190 | Milwaukee | 2.66 | - | 6 | - | 1 | 2 | 30 | published, never ranked (may be uncrawled) |
| 191 | San Diego | 2.77 | 214,939 | 15 | 3 | 2 | - | 60 | published, never ranked (may be uncrawled) |
| 192 | Gdansk | 1.82 | 4,908 | 11 | 8 | 1 | 305 | 30 | published, never ranked (may be uncrawled) |
| 193 | Bled | 2.72 | 13,126 | - | - | - | - | 10 | predicted (travel demand) |
| 194 | Maastricht | 1.34 | 47,763 | 16 | - | 2 | 135 | 20 | published, never ranked (may be uncrawled) |
| 195 | Syracuse | 1.75 | 102,833 | - | - | - | - | 20 | predicted (travel demand) |
| 196 | Oahu | 2.61 | - | 32 | 8 | 4 | - | 30 | published, never ranked (may be uncrawled) |
| 197 | Cartagena | 2.58 | 65,066 | - | - | - | - | 30 | predicted (travel demand) |
| 198 | Atlanta | 2.57 | - | 12 | 1 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 199 | Padua | 1.36 | 54,592 | 14 | 8 | 1 | 12 | 20 | published, never ranked (may be uncrawled) |
| 200 | Bern | 2.51 | 90,627 | - | - | - | - | 20 | predicted (travel demand) |
| 201 | Bali | 2.49 | - | 5 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 202 | Nice | 2.46 | 136,877 | 11 | 7 | 2 | - | 30 | published, never ranked (may be uncrawled) |
| 203 | Valletta | 2.45 | 84,342 | - | - | - | - | 10 | predicted (travel demand) |
| 204 | Cleveland | 2.44 | - | 5 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 205 | Faro | 1.62 | 55,645 | - | - | - | - | 20 | predicted (travel demand) |
| 206 | Tallinn | 1.62 | 124,888 | 9 | 3 | 2 | 42 | 30 | published, never ranked (may be uncrawled) |
| 207 | Vancouver | 2.37 | 351,552 | 7 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 208 | Capri | 1.60 | - | - | - | - | - | 10 | predicted (travel demand) |
| 209 | Dresden | 1.60 | 113,624 | 32 | 25 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 210 | Rio de Janeiro | 2.40 | 279,431 | 6 | - | - | - | 100 | measured |
| 211 | Zurich | 1.59 | 140,788 | 6 | 2 | - | 26 | 30 | published, never ranked (may be uncrawled) |
| 212 | Brno | 1.58 | 63,714 | 8 | 7 | 2 | 34 | 30 | published, never ranked (may be uncrawled) |
| 213 | Athens | 2.31 | 235,429 | 13 | 8 | 2 | - | 30 | published, never ranked (may be uncrawled) |
| 214 | Kilkenny | 1.55 | 34,550 | - | - | - | - | 10 | predicted (travel demand) |
| 215 | Cusco | 2.35 | 87,732 | - | - | - | - | 30 | predicted (travel demand) |
| 216 | Limerick | 1.57 | 90,379 | - | - | - | - | 20 | predicted (travel demand) |
| 217 | Mumbai | 2.34 | 319,236 | 2 | 2 | - | - | 10 | published, never ranked (may be uncrawled) |
| 218 | Trier | 1.56 | 69,369 | - | - | - | 154 | 20 | predicted (travel demand) |
| 219 | Turku | 2.31 | - | 1 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 220 | Aix-en-Provence | 2.26 | 64,524 | - | - | - | - | 20 | predicted (travel demand) |
| 221 | Pisa | 1.46 | 52,174 | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 222 | Nashville | 2.23 | - | 8 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 223 | New Orleans | 2.21 | 256,232 | 9 | 8 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 224 | Istanbul | 1.90 | 333,027 | 14 | 6 | 1 | - | 100 | published, never ranked (may be uncrawled) |
| 225 | Hanoi | 2.15 | 117,396 | 3 | 1 | - | - | 100 | published, never ranked (may be uncrawled) |
| 226 | Ann Arbor | 2.14 | - | 3 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 227 | Nijmegen | 1.05 | 42,338 | 20 | 2 | 3 | 159 | 20 | published, never ranked (may be uncrawled) |
| 228 | Cairo | 2.09 | 176,137 | 1 | 1 | - | - | 100 | published, never ranked (may be uncrawled) |
| 229 | Taipei | 2.09 | 143,193 | 4 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 230 | Adelaide | 2.04 | 139,166 | 3 | 2 | - | - | 60 | published, never ranked (may be uncrawled) |
| 231 | Hiroshima | 1.39 | 129,791 | 33 | 6 | 2 | - | 60 | published, never ranked (may be uncrawled) |
| 232 | Salamanca | 1.37 | 47,897 | 4 | 1 | 1 | 1 | 20 | published, never ranked (may be uncrawled) |
| 233 | La Gomera | 1.37 | - | - | - | - | - | 10 | predicted (travel demand) |
| 234 | Tilburg | 1.03 | - | 17 | - | 3 | 86 | 20 | published, never ranked (may be uncrawled) |
| 235 | Ischia | 1.32 | - | - | - | - | 2 | 20 | predicted (travel demand) |
| 236 | Alkmaar | 1.01 | - | 11 | - | 2 | 79 | 20 | published, never ranked (may be uncrawled) |
| 237 | Albuquerque | 1.96 | - | 1 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 238 | Izmir | 1.88 | 69,826 | - | - | - | - | 60 | predicted (travel demand) |
| 239 | Como | 0.96 | 82,645 | 9 | 3 | 1 | 23 | 20 | published, never ranked (may be uncrawled) |
| 240 | Wroclaw | 1.27 | 123,894 | 5 | 2 | 1 | 121 | 30 | published, never ranked (may be uncrawled) |
| 241 | Buenos Aires | 1.83 | 333,331 | 5 | 3 | - | - | 60 | published, never ranked (may be uncrawled) |
| 242 | Hilversum | 0.93 | - | 6 | 5 | 1 | 122 | 20 | published, never ranked (may be uncrawled) |
| 243 | Bucharest | 1.84 | 136,836 | 4 | - | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 244 | Hobart | 1.23 | 81,734 | 11 | 4 | 2 | 455 | 20 | published, never ranked (may be uncrawled) |
| 245 | Stirling | 1.78 | 43,558 | - | - | - | - | 10 | predicted (travel demand) |
| 246 | Baltimore | 1.77 | - | 5 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 247 | Christchurch | 1.21 | 104,874 | 6 | 2 | 1 | 466 | 30 | published, never ranked (may be uncrawled) |
| 248 | Graz | 1.21 | 65,717 | 17 | 10 | 2 | 87 | 30 | published, never ranked (may be uncrawled) |
| 249 | Sardinia | 0.97 | - | 7 | 6 | - | 10 | 60 | published, never ranked (may be uncrawled) |
| 250 | Auckland | 1.17 | 152,056 | 5 | 3 | - | 977 | 60 | published, never ranked (may be uncrawled) |
| 251 | Dijon | 1.72 | 43,526 | - | - | - | - | 20 | predicted (travel demand) |
| 252 | York | 1.69 | 118,066 | 8 | 6 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 253 | Annecy | 1.69 | 56,859 | - | - | - | - | 20 | predicted (travel demand) |
| 254 | Cagliari | 0.92 | 51,351 | 14 | 1 | 2 | 14 | 20 | published, never ranked (may be uncrawled) |
| 255 | Geneva | 1.13 | 162,269 | 21 | 8 | 4 | 131 | 20 | published, never ranked (may be uncrawled) |
| 256 | Middletown | 1.64 | - | - | - | - | - | 10 | predicted (travel demand) |
| 257 | Liverpool | 1.61 | 248,189 | 4 | 3 | - | - | 30 | published, never ranked (may be uncrawled) |
| 258 | Freiburg | 1.54 | 92,752 | 8 | 4 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 259 | Shanghai | 1.59 | 277,140 | 2 | 2 | - | - | 100 | published, never ranked (may be uncrawled) |
| 260 | Mostar | 1.58 | 63,907 | - | - | - | - | 20 | predicted (travel demand) |
| 261 | Reykjavik | 1.38 | 166,789 | 4 | 3 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 262 | Bristol | 1.52 | 163,983 | 26 | 11 | 3 | - | 30 | published, never ranked (may be uncrawled) |
| 263 | Quebec City | 1.01 | 124,358 | 6 | - | 1 | 494 | 30 | published, never ranked (may be uncrawled) |
| 264 | Savannah | 1.52 | 128,162 | 4 | 2 | - | - | 20 | published, never ranked (may be uncrawled) |
| 265 | Gothenburg | 1.49 | 119,991 | 5 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 266 | Delft | 0.74 | 31,293 | 12 | - | 1 | 60 | 20 | published, never ranked (may be uncrawled) |
| 267 | Cork | 0.97 | 101,405 | 13 | 2 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 268 | Malta | 1.45 | - | 1 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 269 | Parma | 0.80 | 40,425 | 5 | - | 1 | 7 | 20 | published, never ranked (may be uncrawled) |
| 270 | Beijing | 1.43 | 269,737 | 7 | 1 | - | - | 100 | published, never ranked (may be uncrawled) |
| 271 | Dordrecht | 0.71 | - | 17 | 1 | 2 | 105 | 20 | published, never ranked (may be uncrawled) |
| 272 | Thessaloniki | 1.42 | 180,145 | 4 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 273 | Bruges | 1.40 | 106,902 | 4 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 274 | Cadiz | 0.90 | 79,226 | 5 | 4 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 275 | Amersfoort | 0.67 | - | 21 | 1 | 2 | 181 | 20 | published, never ranked (may be uncrawled) |
| 276 | Sapporo | 0.88 | 88,633 | 6 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 277 | Antalya | 1.31 | 70,688 | - | - | - | - | 60 | predicted (travel demand) |
| 278 | Cardiff | 1.27 | - | 13 | 1 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 279 | Santa Fe | 1.29 | - | 3 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 280 | Breda | 0.64 | 36,579 | 11 | 1 | 2 | 120 | 20 | published, never ranked (may be uncrawled) |
| 281 | Colmar | 1.28 | 45,517 | - | - | - | - | 20 | predicted (travel demand) |
| 282 | Madeira | 0.77 | - | 12 | 3 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 283 | Bodrum | 1.26 | 33,918 | - | - | - | - | 20 | predicted (travel demand) |
| 284 | Riga | 1.23 | 108,918 | 5 | 2 | - | - | 30 | published, never ranked (may be uncrawled) |
| 285 | Nafplio | 1.24 | 31,193 | - | - | - | - | 10 | predicted (travel demand) |
| 286 | Lausanne | 1.23 | 68,242 | 8 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 287 | Evora | 0.78 | 15,345 | - | - | - | - | 20 | predicted (travel demand) |
| 288 | Nagoya | 0.79 | 83,437 | 6 | 2 | - | 1 | 60 | published, never ranked (may be uncrawled) |
| 289 | Cyprus | 1.18 | - | 15 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 290 | Palma de Mallorca | 0.71 | 84,075 | 6 | 2 | 1 | 8 | 30 | published, never ranked (may be uncrawled) |
| 291 | Stuttgart | 1.02 | 112,789 | 15 | 7 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 292 | Maui | 1.17 | - | 5 | 2 | - | - | 20 | published, never ranked (may be uncrawled) |
| 293 | Bergamo | 0.57 | 52,933 | 9 | 2 | 1 | 17 | 20 | published, never ranked (may be uncrawled) |
| 294 | Bordeaux | 0.76 | 156,201 | 10 | - | 2 | 211 | 30 | published, never ranked (may be uncrawled) |
| 295 | Menorca | 0.73 | - | 6 | - | - | 2 | 20 | published, never ranked (may be uncrawled) |
| 296 | Zaragoza | 0.73 | 87,580 | 7 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 297 | Toulouse | 0.73 | 112,721 | 10 | - | 1 | 34 | 30 | published, never ranked (may be uncrawled) |
| 298 | Leiden | 0.54 | 33,227 | 19 | 6 | 1 | 129 | 20 | published, never ranked (may be uncrawled) |
| 299 | Okinawa | 0.71 | 24,466 | 6 | - | - | 1 | 30 | published, never ranked (may be uncrawled) |
| 300 | Braga | 0.62 | 34,522 | 8 | 2 | 1 | 8 | 20 | published, never ranked (may be uncrawled) |
| 301 | Apeldoorn | 0.53 | - | 8 | - | 2 | 80 | 20 | published, never ranked (may be uncrawled) |
| 302 | Dubrovnik | 0.99 | 119,586 | 4 | 4 | - | 2 | 10 | published, never ranked (may be uncrawled) |
| 303 | Belfast | 1.04 | 224,315 | 8 | 3 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 304 | Salzburg | 0.68 | 107,243 | 21 | 12 | 3 | 33 | 20 | published, never ranked (may be uncrawled) |
| 305 | Split | 0.97 | 132,399 | 6 | 2 | 1 | 2 | 20 | published, never ranked (may be uncrawled) |
| 306 | Haarlem | 0.50 | 33,960 | 21 | 2 | 2 | 277 | 20 | published, never ranked (may be uncrawled) |
| 307 | Azores | 0.65 | - | 7 | 4 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 308 | Sorrento | 0.49 | 40,049 | 7 | - | 1 | 20 | 10 | published, never ranked (may be uncrawled) |
| 309 | Catania | 0.57 | 58,252 | 4 | 3 | 1 | 5 | 30 | published, never ranked (may be uncrawled) |
| 310 | Kanazawa | 0.63 | 25,778 | 7 | 3 | 1 | 2 | 30 | published, never ranked (may be uncrawled) |
| 311 | Oaxaca | 0.95 | 72,955 | - | - | - | - | 60 | predicted (travel demand) |
| 312 | Nantes | 0.96 | 67,689 | 1 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 313 | Granada | 0.60 | 86,361 | 11 | 4 | 2 | 4 | 20 | published, never ranked (may be uncrawled) |
| 314 | Innsbruck | 0.63 | 58,742 | 6 | 2 | 1 | 39 | 20 | published, never ranked (may be uncrawled) |
| 315 | Arnhem | 0.46 | 31,478 | 32 | 3 | 3 | 202 | 20 | published, never ranked (may be uncrawled) |
| 316 | Rothenburg ob der Tauber | 0.77 | 39,879 | 5 | 1 | 1 | 8 | 10 | published, never ranked (may be uncrawled) |
| 317 | Lucca | 0.45 | 52,271 | 16 | 4 | 1 | 27 | 20 | published, never ranked (may be uncrawled) |
| 318 | Luxembourg City | 0.60 | 64,851 | 10 | 8 | 2 | 18 | 20 | published, never ranked (may be uncrawled) |
| 319 | Crete | 0.86 | - | 4 | 3 | - | - | 30 | published, never ranked (may be uncrawled) |
| 320 | Kotor | 0.86 | 48,982 | 1 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 321 | Segovia | 0.54 | 30,968 | 6 | - | 1 | 5 | 20 | published, never ranked (may be uncrawled) |
| 322 | Brighton | 0.85 | 114,108 | 9 | 4 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 323 | Busan | 0.83 | 94,737 | 2 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 324 | Cape Town | 0.82 | 199,169 | 1 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 325 | Belgrade | 0.83 | 178,116 | 5 | 5 | - | - | 60 | published, never ranked (may be uncrawled) |
| 326 | Verona | 0.48 | 77,646 | 11 | 6 | 1 | 3 | 30 | published, never ranked (may be uncrawled) |
| 327 | Kandy | 0.78 | 24,159 | 2 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 328 | Bath | 0.77 | 144,950 | 9 | 2 | 2 | - | 20 | published, never ranked (may be uncrawled) |
| 329 | Potsdam | 0.51 | 51,727 | 18 | 9 | 3 | 16 | 20 | published, never ranked (may be uncrawled) |
| 330 | Sao Paulo | 0.74 | 911 | 1 | - | - | - | 100 | published, never ranked (may be uncrawled) |
| 331 | Trento | 0.38 | 56,455 | 10 | 2 | 1 | 20 | 20 | published, never ranked (may be uncrawled) |
| 332 | Heidelberg | 0.67 | 75,837 | 10 | 2 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 333 | Ibiza | 0.46 | - | 1 | - | - | 4 | 20 | published, never ranked (may be uncrawled) |
| 334 | Modena | 0.44 | 51,698 | 5 | 1 | 1 | 3 | 20 | published, never ranked (may be uncrawled) |
| 335 | Den Bosch | 0.36 | 39,682 | 11 | 2 | 1 | 118 | 20 | published, never ranked (may be uncrawled) |
| 336 | Ronda | 0.42 | 51,510 | 10 | 1 | - | 10 | 10 | published, never ranked (may be uncrawled) |
| 337 | Assen | 0.35 | - | 9 | - | 2 | 66 | 20 | published, never ranked (may be uncrawled) |
| 338 | Heerlen | 0.35 | - | 8 | 1 | 2 | 53 | 20 | published, never ranked (may be uncrawled) |
| 339 | Kamakura | 0.44 | 33,492 | 7 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 340 | Zwolle | 0.35 | - | 15 | 4 | 3 | 58 | 20 | published, never ranked (may be uncrawled) |
| 341 | Inverness | 0.69 | 92,195 | 1 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 342 | Corfu | 0.68 | 139,334 | 8 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 343 | Coimbra | 0.36 | 34,962 | 6 | - | - | 5 | 20 | published, never ranked (may be uncrawled) |
| 344 | Cordoba | 0.41 | 74,675 | 17 | 2 | 2 | 3 | 30 | published, never ranked (may be uncrawled) |
| 345 | Gran Canaria | 0.42 | - | 10 | 4 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 346 | Hallstatt | 0.50 | 47,271 | 8 | 4 | - | 4 | 10 | published, never ranked (may be uncrawled) |
| 347 | Guimaraes | 0.32 | 26,203 | 10 | 1 | 1 | 19 | 20 | published, never ranked (may be uncrawled) |
| 348 | Ghent | 0.59 | 82,757 | 8 | 2 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 349 | Hoorn | 0.30 | - | 12 | - | 2 | 52 | 20 | published, never ranked (may be uncrawled) |
| 350 | Leeuwarden | 0.30 | - | 34 | - | 2 | 61 | 20 | published, never ranked (may be uncrawled) |
| 351 | Lima | 0.51 | 132,792 | 5 | 1 | 1 | - | 100 | published, never ranked (may be uncrawled) |
| 352 | Rouen | 0.54 | 72,334 | 12 | - | 1 | 6 | 20 | published, never ranked (may be uncrawled) |
| 353 | Helmond | 0.29 | - | 19 | - | 2 | 54 | 20 | published, never ranked (may be uncrawled) |
| 354 | Tarragona | 0.36 | 32,396 | 5 | 3 | - | - | 20 | published, never ranked (may be uncrawled) |
| 355 | Pamplona | 0.34 | 128,065 | 25 | 1 | 3 | 9 | 20 | published, never ranked (may be uncrawled) |
| 356 | Perugia | 0.29 | 42,572 | 16 | 1 | 2 | 19 | 20 | published, never ranked (may be uncrawled) |
| 357 | Phoenix | 0.55 | - | - | - | - | - | 60 | predicted (travel demand) |
| 358 | Roosendaal | 0.26 | - | 20 | - | 2 | 138 | 20 | published, never ranked (may be uncrawled) |
| 359 | Cesky Krumlov | 0.34 | 28,582 | 6 | 3 | - | 11 | 10 | published, never ranked (may be uncrawled) |
| 360 | Leuven | 0.51 | 40,645 | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 361 | Killarney | 0.30 | 28,763 | 1 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 362 | Yakushima | 0.28 | - | 4 | 4 | - | 1 | 10 | published, never ranked (may be uncrawled) |
| 363 | Matera | 0.25 | 67,033 | 4 | - | - | 2 | 20 | published, never ranked (may be uncrawled) |
| 364 | Canterbury | 0.40 | 53,301 | 4 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 365 | Zadar | 0.38 | 71,549 | 1 | - | - | 1 | 20 | published, never ranked (may be uncrawled) |
| 366 | Ferrara | 0.21 | 27,490 | 6 | 4 | 1 | 7 | 20 | published, never ranked (may be uncrawled) |
| 367 | Toledo | 0.24 | 3,149 | - | - | - | - | 20 | predicted (travel demand) |
| 368 | Setubal | 0.19 | 22,582 | 10 | 5 | 2 | 13 | 20 | published, never ranked (may be uncrawled) |
| 369 | Anuradhapura | 0.32 | - | 1 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 370 | Caserta | 0.16 | 14,783 | 24 | - | 1 | 51 | 20 | published, never ranked (may be uncrawled) |
| 371 | Regensburg | 0.30 | 51,930 | 8 | 2 | 1 | 3 | 20 | published, never ranked (may be uncrawled) |
| 372 | Bamberg | 0.24 | 28,716 | 11 | 7 | 1 | 15 | 20 | published, never ranked (may be uncrawled) |
| 373 | Newark | 0.29 | - | - | - | - | - | 10 | predicted (travel demand) |
| 374 | Assisi | 0.17 | 30,278 | 6 | 1 | 2 | 6 | 10 | published, never ranked (may be uncrawled) |
| 375 | Stratford-upon-Avon | 0.27 | 68,555 | 2 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 376 | La Palma | 0.17 | - | 4 | 3 | - | - | 20 | published, never ranked (may be uncrawled) |
| 377 | Oss | 0.11 | - | 5 | - | - | 48 | 20 | published, never ranked (may be uncrawled) |
| 378 | Queenstown | 0.16 | 36,672 | - | - | - | - | 10 | predicted (travel demand) |
| 379 | San Juan | 0.15 | - | - | - | - | - | 10 | predicted (travel demand) |
| 380 | Windsor | 0.13 | 30,452 | 2 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 381 | Halifax | 0.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 382 | Memphis | 0.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 383 | George Town | 0.07 | 36,080 | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 384 | Allentown | 0.06 | - | 1 | - | - | 3 | 20 | published, never ranked (may be uncrawled) |
| 385 | Buffalo | 0.04 | - | 1 | - | - | - | 10 | published, never ranked (may be uncrawled) |

## What this replaces

All of these named a city order and are now superseded. Deleting them is the
point of this file; leaving them is how six orders happened.

- CLAUDE.md Step 0 rung 4, "the recorded wave order" (data-led, register-first).
- CLAUDE.md "TOP OF THE QUEUE, ruled 2026-08-09: Porto and Lisbon". Not
  contradicted, absorbed: they come out 1 and 2 on the measured evidence.
- CLAUDE.md "Current focus, 2026-08-06: the tourist-city rollout, London
  first", and its phase-1 list of ten.
- CLAUDE.md "The working order, re-ruled 2026-08-06", the five numbered pairs.
- .github/workflows/nightly.yml, which carries its own order in the run prompt
  ("Barcelona, Rome, Paris, Berlin, Amsterdam, New York...") and its own focus
  countries ("Spain, Japan, Portugal. Italy is next").
- data/city-list.json ranks 1-25, which are rollout-25.json's order.

Two things survive untouched because they are not orderings: the London gate
(no Woodland Trust data without written permission) and the small-city stop
insofar as it means not opening new villages, which this list enforces anyway
by scoring them near zero.

