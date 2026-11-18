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
| 1 | Lisbon | 83.45 | 201,877 | 38 | 23 | 3 | 67 | 30 | measured |
| 2 | Seville | 77.98 | 170,545 | 44 | 12 | 2 | - | 30 | measured |
| 3 | Berlin | 56.09 | 412,181 | 63 | 51 | 5 | 195 | 60 | measured |
| 4 | Tokyo | 45.15 | 394,702 | 22 | 16 | 1 | 5 | 100 | measured |
| 5 | Palermo | 32.83 | 124,310 | 27 | 14 | 3 | 38 | 30 | measured |
| 6 | Malaga | 42.41 | 117,780 | 10 | 5 | 1 | - | 30 | measured |
| 7 | Monterey | 62.93 | - | 3 | 2 | - | - | 10 | measured |
| 8 | San Francisco | 41.04 | 361,111 | 12 | 3 | 1 | 26 | 30 | measured |
| 9 | Singapore | 39.67 | 967,821 | 34 | 7 | 3 | 165 | 100 | measured |
| 10 | Amsterdam | 28.73 | 294,030 | 27 | 8 | 2 | 5488 | 30 | measured |
| 11 | Munich | 35.57 | 224,067 | 63 | 36 | 8 | 74 | 60 | measured |
| 12 | Tenerife | 34.20 | - | 9 | 6 | - | - | 30 | measured |
| 13 | Kyoto | 32.83 | 142,353 | 18 | 15 | 2 | - | 60 | measured |
| 14 | Paris | 32.83 | 524,268 | 58 | 15 | 8 | 129 | 60 | measured |
| 15 | Barcelona | 23.26 | 346,477 | 59 | 21 | 7 | 180 | 60 | measured |
| 16 | London | 39.67 | 718,291 | 53 | 43 | 2 | - | 100 | measured |
| 17 | Austin | 43.78 | 226,631 | 12 | 5 | 1 | - | 30 | measured |
| 18 | Venice | 21.89 | 267,527 | 11 | 6 | 2 | 4 | 30 | measured |
| 19 | Los Angeles | 38.31 | 665,559 | 20 | 6 | 1 | - | 60 | measured |
| 20 | Oahu | 38.31 | - | 32 | 8 | 4 | - | 30 | measured |
| 21 | Milan | 19.15 | 212,705 | 30 | 14 | 3 | 25 | 60 | measured |
| 22 | Porto | 19.15 | 120,415 | 32 | 16 | 3 | 40 | 30 | measured |
| 23 | Birmingham | 37.53 | - | - | - | - | - | 60 | predicted (travel demand) |
| 24 | Charleston | 32.83 | 155,987 | 4 | 1 | - | - | 20 | measured |
| 25 | Seoul | 28.73 | 206,265 | 8 | 5 | 1 | - | 100 | measured |
| 26 | Brisbane | 20.52 | 162,602 | 21 | 6 | 2 | 186 | 60 | measured |
| 27 | Copenhagen | 28.73 | 218,621 | 49 | 41 | 6 | - | 30 | measured |
| 28 | Prague | 19.15 | 303,350 | 30 | 21 | 4 | 31 | 60 | measured |
| 29 | Dublin | 16.42 | 240,850 | 20 | 5 | 2 | 12 | 30 | measured |
| 30 | Seattle | 27.36 | 398,724 | 30 | 3 | 4 | - | 30 | measured |
| 31 | Reykjavik | 24.63 | 166,789 | 4 | 3 | 1 | - | 20 | measured |
| 32 | New York | 24.63 | 1,124,326 | 98 | 11 | 8 | - | 100 | measured |
| 33 | Madrid | 16.42 | 274,553 | 18 | 11 | 2 | - | 60 | measured |
| 34 | Kanazawa | 16.42 | 25,778 | 7 | 3 | 1 | 2 | 30 | measured |
| 35 | Florence | 12.31 | 184,099 | 29 | 9 | 1 | 27 | 30 | measured |
| 36 | Fukuoka | 15.05 | 77,485 | 18 | 11 | 1 | - | 60 | measured |
| 37 | Rome | 10.94 | 358,876 | 32 | 11 | 2 | 31 | 60 | measured |
| 38 | Edinburgh | 20.52 | 292,981 | 22 | 12 | 1 | - | 30 | measured |
| 39 | Long Beach | 20.48 | - | - | - | - | - | 30 | predicted (travel demand) |
| 40 | Little Rock | 20.40 | - | - | - | - | - | 20 | predicted (travel demand) |
| 41 | Alicante | 9.58 | 77,454 | 21 | 4 | 2 | 44 | 30 | measured |
| 42 | Leiden | 9.58 | 33,227 | 19 | 6 | 1 | 129 | 20 | measured |
| 43 | Cambridge | 19.15 | 97,974 | 10 | 2 | 1 | - | 20 | measured |
| 44 | Reno | 18.19 | - | - | - | - | - | 30 | predicted (travel demand) |
| 45 | Athens | 17.79 | 235,429 | 12 | 7 | 2 | - | 30 | measured |
| 46 | Des Moines | 18.11 | - | - | - | - | - | 20 | predicted (travel demand) |
| 47 | Philadelphia | 16.42 | 405,294 | 13 | 1 | - | - | 60 | measured |
| 48 | Daytona Beach | 17.66 | - | - | - | - | - | 20 | predicted (travel demand) |
| 49 | Sardinia | 9.58 | - | 7 | 6 | - | 10 | 60 | measured |
| 50 | Dallas | 16.42 | - | 12 | 2 | 1 | - | 60 | measured |
| 51 | Naples | 8.21 | 198,913 | 31 | 5 | 3 | 47 | 30 | measured |
| 52 | New Orleans | 16.42 | 256,232 | 8 | 7 | 1 | - | 30 | measured |
| 53 | Utrecht | 8.21 | 67,963 | 30 | 9 | 2 | 339 | 30 | measured |
| 54 | Valencia | 8.21 | 162,209 | 31 | 4 | 2 | 350 | 30 | measured |
| 55 | Huntsville | 15.35 | - | - | - | - | - | 20 | predicted (travel demand) |
| 56 | Saratoga Springs | 15.05 | - | - | - | - | - | 10 | predicted (travel demand) |
| 57 | West Palm Beach | 14.98 | - | - | - | - | - | 20 | predicted (travel demand) |
| 58 | Saint Petersburg | 14.83 | - | - | - | - | - | 100 | predicted (travel demand) |
| 59 | Geneva | 9.58 | 162,269 | 21 | 8 | 4 | 131 | 20 | measured |
| 60 | Melbourne | 9.58 | 267,898 | 19 | 6 | 2 | 391 | 100 | measured |
| 61 | Ottawa | 9.58 | - | 21 | - | 3 | 122 | 60 | measured |
| 62 | Vilnius | 9.58 | 113,188 | 12 | 4 | 1 | 34 | 30 | measured |
| 63 | Zurich | 9.58 | 140,788 | 6 | 2 | - | 26 | 30 | measured |
| 64 | Girona | 8.21 | 51,072 | 7 | 3 | - | - | 20 | measured |
| 65 | Antwerp | 13.68 | 128,289 | 10 | 4 | 1 | - | 30 | measured |
| 66 | Bristol | 13.68 | 163,983 | 22 | 5 | 1 | - | 30 | measured |
| 67 | Sintra | 6.84 | 46,889 | 8 | 6 | 1 | 6 | 30 | measured |
| 68 | Palma de Mallorca | 8.21 | 84,075 | 6 | 2 | 1 | 8 | 30 | measured |
| 69 | Freiburg | 12.31 | 92,752 | 8 | 4 | 1 | - | 20 | measured |
| 70 | Cagliari | 6.84 | 51,351 | 14 | 1 | 2 | 14 | 20 | measured |
| 71 | Detroit | 12.53 | - | - | - | - | - | 30 | predicted (travel demand) |
| 72 | Stuttgart | 10.94 | 112,789 | 11 | 7 | - | - | 30 | measured |
| 73 | Genoa | 6.84 | 145,206 | 13 | 2 | 1 | 10 | 30 | measured |
| 74 | Brussels | 8.21 | 176,863 | 35 | 4 | 2 | 436 | 60 | measured |
| 75 | Portland | 8.21 | 217,222 | 33 | 2 | 3 | 306 | 30 | measured |
| 76 | Vienna | 8.21 | 283,090 | 61 | 25 | 6 | 358 | 60 | measured |
| 77 | Montreal | 12.31 | 315,322 | 14 | 2 | 2 | - | 60 | measured |
| 78 | Fort Worth | 10.94 | - | 29 | - | 2 | - | 30 | measured |
| 79 | Spokane | 8.21 | - | 18 | - | 2 | 18 | 20 | measured |
| 80 | Jerusalem | 11.17 | 314,788 | - | - | - | - | 60 | predicted (travel demand) |
| 81 | Oxford | 10.94 | 111,583 | 7 | 2 | 1 | - | 20 | measured |
| 82 | Perth | 10.94 | 180,478 | 6 | 4 | 1 | - | 60 | measured |
| 83 | Dubai | 11.02 | 334,167 | - | - | - | - | 60 | predicted (travel demand) |
| 84 | Groningen | 5.47 | 31,401 | 17 | 5 | 2 | 76 | 20 | measured |
| 85 | Leeuwarden | 5.47 | - | 34 | - | 2 | 61 | 20 | measured |
| 86 | Osaka | 6.84 | 163,112 | 6 | 1 | - | - | 60 | measured |
| 87 | Jersey City | 10.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 88 | Helsinki | 8.21 | 148,908 | 12 | 3 | 1 | 13 | 30 | measured |
| 89 | Krakow | 6.84 | 140,824 | 38 | 11 | 3 | 198 | 30 | measured |
| 90 | Anchorage | 10.25 | - | - | - | - | - | 30 | predicted (travel demand) |
| 91 | Raleigh | 10.07 | - | - | - | - | - | 30 | predicted (travel demand) |
| 92 | Coimbra | 5.47 | 34,962 | 6 | - | - | 5 | 20 | measured |
| 93 | El Paso | 9.70 | - | - | - | - | - | 30 | predicted (travel demand) |
| 94 | Santorini | 9.63 | - | - | - | - | - | 10 | predicted (travel demand) |
| 95 | Edmonton | 9.38 | - | - | - | - | - | 60 | predicted (travel demand) |
| 96 | Winnipeg | 9.21 | - | - | - | - | - | 30 | predicted (travel demand) |
| 97 | Madeira | 5.47 | - | 11 | 2 | 1 | - | 30 | measured |
| 98 | Tampere | 8.78 | - | - | - | - | - | 30 | predicted (travel demand) |
| 99 | Segovia | 5.47 | 30,968 | 6 | - | 1 | 5 | 20 | measured |
| 100 | Hamburg | 8.21 | 191,221 | 6 | 4 | 1 | - | 60 | measured |
| 101 | Granada | 5.47 | 86,361 | 11 | 5 | 2 | 4 | 20 | measured |
| 102 | Cadiz | 5.47 | 79,226 | 5 | 4 | 1 | - | 20 | measured |
| 103 | Bordeaux | 5.47 | 156,201 | 10 | - | 2 | 211 | 30 | measured |
| 104 | Christchurch | 5.47 | 104,874 | 6 | 2 | 1 | 466 | 30 | measured |
| 105 | Indianapolis | 8.21 | - | 5 | 1 | - | - | 30 | measured |
| 106 | Leipzig | 5.47 | 121,319 | 31 | 24 | 4 | - | 30 | measured |
| 107 | Lyon | 5.47 | 136,951 | 34 | 4 | 6 | 178 | 30 | measured |
| 108 | San Diego | 8.21 | 214,939 | 13 | 1 | 2 | - | 60 | measured |
| 109 | Amersfoort | 4.10 | - | 21 | 1 | 2 | 181 | 20 | measured |
| 110 | Venlo | 4.10 | - | 7 | - | 1 | 144 | 20 | measured |
| 111 | Luang Prabang | 7.49 | 24,534 | - | - | - | - | 20 | predicted (travel demand) |
| 112 | Bergen | 7.30 | 82,940 | - | - | - | - | 30 | predicted (travel demand) |
| 113 | Sydney | 6.84 | 305,304 | 8 | 4 | - | - | 100 | measured |
| 114 | Gyeongju | 6.94 | 30,260 | - | - | - | - | 20 | predicted (travel demand) |
| 115 | Siena | 4.62 | 57,436 | - | - | - | - | 20 | predicted (travel demand) |
| 116 | Verona | 4.10 | 77,646 | 9 | 4 | 1 | 3 | 30 | measured |
| 117 | Santiago de Compostela | 4.52 | 93,477 | - | - | - | - | 20 | predicted (travel demand) |
| 118 | Frankfurt | 4.51 | 150,379 | 28 | 13 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 119 | Zagreb | 6.42 | 122,890 | - | - | - | - | 30 | predicted (travel demand) |
| 120 | Bogota | 6.39 | 1,623 | - | - | - | - | 100 | predicted (travel demand) |
| 121 | Shanghai | 6.38 | 277,140 | - | - | - | - | 100 | predicted (travel demand) |
| 122 | Funchal | 3.77 | 174,351 | - | - | - | - | 20 | predicted (travel demand) |
| 123 | Graz | 4.10 | 65,717 | 17 | 10 | 2 | 87 | 30 | measured |
| 124 | Nuremberg | 4.10 | 161,614 | 20 | 8 | 2 | 37 | 30 | measured |
| 125 | Tallinn | 4.10 | 124,888 | 9 | 3 | 2 | 42 | 30 | measured |
| 126 | Houston | 6.11 | - | 12 | 2 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 127 | Washington DC | 5.47 | 606,731 | 34 | 8 | 4 | - | 30 | measured |
| 128 | Alice Springs | 5.71 | - | - | - | - | - | 10 | predicted (travel demand) |
| 129 | Jacksonville | 5.69 | - | 2 | 2 | - | - | 30 | published, never ranked (may be uncrawled) |
| 130 | Avignon | 5.54 | 64,047 | - | - | - | - | 20 | predicted (travel demand) |
| 131 | Alkmaar | 2.74 | - | 11 | - | 2 | 79 | 20 | measured |
| 132 | Caserta | 2.74 | 14,783 | 24 | - | 1 | 51 | 20 | measured |
| 133 | Dordrecht | 2.74 | - | 17 | 1 | 2 | 105 | 20 | measured |
| 134 | Eindhoven | 2.74 | - | 17 | - | 3 | 195 | 20 | measured |
| 135 | Hilversum | 2.74 | - | 6 | 2 | 1 | 122 | 20 | measured |
| 136 | Nijmegen | 2.74 | 42,338 | 20 | 1 | 3 | 159 | 20 | measured |
| 137 | Rotterdam | 2.74 | 104,938 | 17 | 1 | 2 | 83 | 30 | measured |
| 138 | Trieste | 2.74 | 117,233 | 36 | 1 | 3 | 43 | 20 | measured |
| 139 | Bruges | 5.47 | 106,902 | 4 | - | 1 | - | 20 | measured |
| 140 | Cologne | 5.47 | 191,812 | 5 | - | 1 | - | 60 | measured |
| 141 | Galway | 3.65 | 88,162 | - | - | - | - | 20 | predicted (travel demand) |
| 142 | Maui | 5.47 | - | 5 | 2 | - | - | 20 | measured |
| 143 | Phuket | 5.46 | 5,487 | - | - | - | - | 30 | predicted (travel demand) |
| 144 | Rovaniemi | 5.38 | - | - | - | - | - | 20 | predicted (travel demand) |
| 145 | Aarhus | 5.23 | 52,722 | 7 | 1 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 146 | Lagos | 3.43 | 34,452 | - | - | - | - | 100 | predicted (travel demand) |
| 147 | Guimaraes | 2.74 | 26,203 | 10 | 1 | 1 | 19 | 20 | measured |
| 148 | Asheville | 5.22 | - | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 149 | Lund | 5.14 | - | - | - | - | - | 20 | predicted (travel demand) |
| 150 | Bologna | 2.74 | 146,161 | 14 | 9 | 1 | 9 | 30 | measured |
| 151 | Kobe | 3.40 | 54,798 | - | - | - | - | 60 | predicted (travel demand) |
| 152 | Boise | 5.07 | - | 4 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 153 | Fort Lauderdale | 4.61 | - | 10 | - | - | 3 | 20 | published, never ranked (may be uncrawled) |
| 154 | Heraklion | 4.96 | 66,359 | - | - | - | - | 20 | predicted (travel demand) |
| 155 | Marseille | 4.96 | 182,033 | - | - | - | - | 30 | predicted (travel demand) |
| 156 | Beijing | 4.79 | 269,737 | 7 | 1 | - | - | 100 | measured |
| 157 | Rio de Janeiro | 4.79 | 279,431 | 6 | - | - | - | 100 | measured |
| 158 | Lexington | 4.56 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 159 | Ronda | 2.74 | 51,510 | 10 | 1 | - | 10 | 10 | measured |
| 160 | Oakland | 4.70 | - | 4 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 161 | Bari | 2.74 | 86,456 | 5 | 1 | - | 8 | 30 | measured |
| 162 | Basel | 4.59 | 105,838 | - | - | - | - | 20 | predicted (travel demand) |
| 163 | Key West | 3.95 | - | 4 | 3 | 1 | 7 | 10 | published, never ranked (may be uncrawled) |
| 164 | Boston | 4.28 | 385,902 | 40 | 6 | 4 | - | 30 | published, never ranked (may be uncrawled) |
| 165 | Tasmania | 4.41 | - | - | - | - | - | 30 | predicted (travel demand) |
| 166 | Ibiza | 2.74 | - | 1 | - | - | 4 | 20 | measured |
| 167 | Ravenna | 2.77 | 86,471 | - | - | - | 1 | 20 | predicted (travel demand) |
| 168 | Cordoba | 2.74 | 74,675 | 17 | 2 | 2 | 3 | 30 | measured |
| 169 | Ghent | 4.10 | 82,757 | 8 | 2 | 1 | - | 30 | measured |
| 170 | Mexico City | 4.10 | 566,583 | 10 | 3 | - | - | 100 | measured |
| 171 | Sofia | 2.81 | 138,710 | 4 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 172 | San Sebastian | 2.80 | 367 | - | - | - | - | 20 | predicted (travel demand) |
| 173 | Chattanooga | 4.17 | - | 2 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 174 | Nagoya | 2.74 | 83,437 | 6 | 2 | - | 1 | 60 | measured |
| 175 | Hong Kong | 2.74 | 689,212 | 21 | 6 | 2 | 505 | 100 | measured |
| 176 | Warsaw | 2.74 | 197,929 | 39 | 21 | 4 | 1407 | 60 | measured |
| 177 | Crete | 4.10 | - | 4 | 3 | - | - | 30 | measured |
| 178 | Tel Aviv | 4.09 | 177,885 | - | - | - | - | 30 | predicted (travel demand) |
| 179 | Interlaken | 4.06 | 24,936 | - | - | - | - | 10 | predicted (travel demand) |
| 180 | Santa Cruz | 4.01 | - | 2 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 181 | Salt Lake City | 2.58 | - | 20 | - | 2 | 29 | 20 | published, never ranked (may be uncrawled) |
| 182 | Taormina | 2.35 | 33,169 | - | - | - | 5 | 10 | predicted (travel demand) |
| 183 | Niagara Falls | 3.68 | - | - | - | - | - | 20 | predicted (travel demand) |
| 184 | Kuala Lumpur | 3.80 | 191,800 | - | - | - | - | 100 | predicted (travel demand) |
| 185 | Bratislava | 2.49 | 132,162 | 7 | 1 | 1 | 26 | 30 | published, never ranked (may be uncrawled) |
| 186 | St. Louis | 3.70 | - | 6 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 187 | Strasbourg | 2.45 | 154,700 | 10 | 2 | 2 | 66 | 30 | published, never ranked (may be uncrawled) |
| 188 | Kauai | 3.67 | - | 9 | 2 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 189 | Wellington | 3.60 | 132,267 | - | - | - | - | 20 | predicted (travel demand) |
| 190 | Tampa | 3.52 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 191 | Montpellier | 3.47 | 64,238 | - | - | - | - | 30 | predicted (travel demand) |
| 192 | Cape Town | 3.29 | 199,169 | - | - | - | - | 60 | predicted (travel demand) |
| 193 | Rhodes | 3.42 | 127,205 | - | - | - | - | 20 | predicted (travel demand) |
| 194 | Cincinnati | 3.33 | - | 8 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 195 | San Antonio | 3.32 | - | 5 | 1 | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 196 | Chania | 3.30 | 47,379 | - | - | - | - | 20 | predicted (travel demand) |
| 197 | Hilo | 3.27 | - | 9 | - | 2 | - | 10 | published, never ranked (may be uncrawled) |
| 198 | Lansing | 3.25 | - | 2 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 199 | Santiago | 3.25 | 111,647 | - | - | - | - | 100 | predicted (travel demand) |
| 200 | Miami | 2.37 | 278,558 | 15 | 1 | 1 | 17 | 30 | published, never ranked (may be uncrawled) |
| 201 | Sarajevo | 3.15 | 205,074 | - | - | - | - | 30 | predicted (travel demand) |
| 202 | Oslo | 2.74 | 181,113 | 5 | 4 | 1 | - | 30 | measured |
| 203 | Lucerne | 3.10 | 66,356 | - | - | - | - | 20 | predicted (travel demand) |
| 204 | Malmo | 3.07 | 103,940 | - | - | - | - | 30 | predicted (travel demand) |
| 205 | Lille | 3.06 | 73,435 | - | - | - | - | 20 | predicted (travel demand) |
| 206 | Bangkok | 2.74 | 222,206 | 6 | 1 | 1 | 5 | 100 | measured |
| 207 | Chicago | 2.74 | 485,769 | 55 | 2 | 6 | 5 | 60 | measured |
| 208 | Tulsa | 3.01 | - | 2 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 209 | Corsica | 3.00 | - | - | - | - | - | 30 | predicted (travel demand) |
| 210 | Mechelen | 2.93 | 20,707 | - | - | - | - | 20 | predicted (travel demand) |
| 211 | Turin | 1.49 | 147,456 | 11 | 10 | 2 | 30 | 30 | published, never ranked (may be uncrawled) |
| 212 | Chiang Mai | 2.85 | 66,541 | 2 | 1 | - | 2 | 60 | published, never ranked (may be uncrawled) |
| 213 | Denver | 2.91 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 214 | Bilbao | 1.93 | 133,133 | 4 | 4 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 215 | San Jose | 2.85 | - | 2 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 216 | Poznan | 1.89 | 65,666 | 10 | - | 1 | 397 | 30 | published, never ranked (may be uncrawled) |
| 217 | Sacramento | 2.83 | - | 2 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 218 | Glasgow | 2.74 | 253,705 | 10 | 6 | - | - | 30 | measured |
| 219 | Pittsburgh | 2.74 | - | 12 | - | 1 | - | 30 | measured |
| 220 | Toronto | 2.74 | 411,011 | 7 | 1 | - | - | 60 | measured |
| 221 | Milwaukee | 2.66 | - | 6 | - | 1 | 2 | 30 | published, never ranked (may be uncrawled) |
| 222 | Como | 1.37 | 82,645 | 9 | 3 | 1 | 23 | 20 | measured |
| 223 | Cyprus | 2.74 | - | 15 | - | - | - | 60 | measured |
| 224 | Deventer | 1.37 | - | 12 | - | 1 | 213 | 20 | measured |
| 225 | Hawaii | 2.74 | - | 8 | - | 1 | - | 60 | measured |
| 226 | Helmond | 1.37 | - | 19 | - | 2 | 54 | 20 | measured |
| 227 | Kansas City | 2.74 | - | 5 | - | 1 | - | 30 | measured |
| 228 | Las Vegas | 2.74 | - | 11 | 6 | 2 | - | 30 | measured |
| 229 | Liverpool | 2.74 | 248,189 | 4 | 3 | - | - | 30 | measured |
| 230 | Savannah | 2.74 | 128,162 | 3 | 1 | - | - | 20 | measured |
| 231 | The Hague | 1.37 | 236,723 | 26 | 4 | 5 | 166 | 30 | measured |
| 232 | Gdansk | 1.82 | 4,908 | 12 | 5 | 1 | 307 | 30 | published, never ranked (may be uncrawled) |
| 233 | Bled | 2.72 | 13,126 | - | - | - | - | 10 | predicted (travel demand) |
| 234 | Maastricht | 1.34 | 47,763 | 16 | - | 2 | 135 | 20 | published, never ranked (may be uncrawled) |
| 235 | Syracuse | 1.75 | 102,833 | - | - | - | - | 20 | predicted (travel demand) |
| 236 | Cartagena | 2.58 | 65,066 | - | - | - | - | 30 | predicted (travel demand) |
| 237 | Atlanta | 2.57 | - | 11 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 238 | Padua | 1.37 | 54,592 | 14 | 8 | 1 | 12 | 20 | measured |
| 239 | Bern | 2.51 | 90,627 | - | - | - | - | 20 | predicted (travel demand) |
| 240 | Bali | 2.49 | - | 5 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 241 | Valletta | 2.45 | 84,342 | - | - | - | - | 10 | predicted (travel demand) |
| 242 | Cleveland | 2.44 | - | 5 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 243 | Faro | 1.62 | 55,645 | - | - | - | - | 20 | predicted (travel demand) |
| 244 | Capri | 1.60 | - | - | - | - | - | 10 | predicted (travel demand) |
| 245 | Dresden | 1.60 | 113,624 | 32 | 25 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 246 | Brno | 1.58 | 63,714 | 8 | 7 | 2 | 34 | 30 | published, never ranked (may be uncrawled) |
| 247 | Braga | 1.37 | 34,522 | 8 | 2 | 1 | 8 | 20 | measured |
| 248 | Ferrara | 1.37 | 27,490 | 6 | 4 | 1 | 7 | 20 | measured |
| 249 | Kilkenny | 1.55 | 34,550 | - | - | - | - | 10 | predicted (travel demand) |
| 250 | Cusco | 2.35 | 87,732 | - | - | - | - | 30 | predicted (travel demand) |
| 251 | Limerick | 1.57 | 90,379 | - | - | - | - | 20 | predicted (travel demand) |
| 252 | Trier | 1.56 | 69,369 | - | - | - | 154 | 20 | predicted (travel demand) |
| 253 | Turku | 2.31 | - | 1 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 254 | Aix-en-Provence | 2.26 | 64,524 | - | - | - | - | 20 | predicted (travel demand) |
| 255 | Pisa | 1.46 | 52,174 | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 256 | Nashville | 2.23 | - | 8 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 257 | Hanoi | 2.15 | 117,396 | 3 | - | - | - | 100 | published, never ranked (may be uncrawled) |
| 258 | Ann Arbor | 2.14 | - | 3 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 259 | Menorca | 1.37 | - | 6 | - | - | 2 | 20 | measured |
| 260 | Taipei | 2.09 | 143,193 | 4 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 261 | Adelaide | 2.04 | 139,166 | 3 | 2 | - | - | 60 | published, never ranked (may be uncrawled) |
| 262 | Salamanca | 1.37 | 47,897 | 4 | 1 | 1 | 1 | 20 | published, never ranked (may be uncrawled) |
| 263 | Canberra | 1.37 | - | 8 | 1 | 1 | 132 | 30 | measured |
| 264 | Cesky Krumlov | 1.37 | 28,582 | 6 | 3 | - | 11 | 10 | measured |
| 265 | Hiroshima | 1.37 | 129,791 | 33 | 6 | 2 | - | 60 | measured |
| 266 | La Gomera | 1.37 | - | - | - | - | - | 10 | predicted (travel demand) |
| 267 | Luxembourg City | 1.37 | 64,851 | 10 | 8 | 2 | 18 | 20 | measured |
| 268 | Salzburg | 1.37 | 107,243 | 21 | 12 | 3 | 33 | 20 | measured |
| 269 | Tilburg | 1.03 | - | 17 | - | 3 | 86 | 20 | published, never ranked (may be uncrawled) |
| 270 | Wroclaw | 1.37 | 123,894 | 5 | 2 | 1 | 121 | 30 | measured |
| 271 | Ischia | 1.32 | - | - | - | - | 2 | 20 | predicted (travel demand) |
| 272 | Albuquerque | 1.96 | - | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 273 | Izmir | 1.88 | 69,826 | - | - | - | - | 60 | predicted (travel demand) |
| 274 | Minneapolis | 1.88 | - | 4 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 275 | Baltimore | 1.77 | - | 5 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 276 | Bucharest | 1.84 | 136,836 | 4 | - | 1 | - | 60 | published, never ranked (may be uncrawled) |
| 277 | Hobart | 1.23 | 81,734 | 11 | 4 | 2 | 455 | 20 | published, never ranked (may be uncrawled) |
| 278 | Stirling | 1.78 | 43,558 | - | - | - | - | 10 | predicted (travel demand) |
| 279 | Auckland | 1.17 | 152,056 | 5 | 2 | - | 977 | 60 | published, never ranked (may be uncrawled) |
| 280 | Dijon | 1.72 | 43,526 | - | - | - | - | 20 | predicted (travel demand) |
| 281 | Stockholm | 1.37 | 188,184 | 8 | 7 | - | - | 30 | measured |
| 282 | Annecy | 1.69 | 56,859 | - | - | - | - | 20 | predicted (travel demand) |
| 283 | Middletown | 1.64 | - | - | - | - | - | 10 | predicted (travel demand) |
| 284 | Rothenburg ob der Tauber | 1.37 | 39,879 | 5 | 1 | 1 | 8 | 10 | measured |
| 285 | Mostar | 1.58 | 63,907 | - | - | - | - | 20 | predicted (travel demand) |
| 286 | Istanbul | 1.37 | 333,027 | 14 | 6 | 1 | - | 100 | measured |
| 287 | Quebec City | 1.01 | 124,358 | 6 | - | 1 | 494 | 30 | published, never ranked (may be uncrawled) |
| 288 | Gothenburg | 1.49 | 119,991 | 5 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 289 | Delft | 0.74 | 31,293 | 12 | - | 1 | 60 | 20 | published, never ranked (may be uncrawled) |
| 290 | Cork | 0.97 | 101,405 | 13 | 2 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 291 | Malta | 1.45 | - | 1 | 1 | - | - | 30 | published, never ranked (may be uncrawled) |
| 292 | Parma | 0.80 | 40,425 | 5 | - | 1 | 7 | 20 | published, never ranked (may be uncrawled) |
| 293 | Budapest | 1.37 | 283,807 | 13 | 2 | 3 | - | 60 | measured |
| 294 | Buenos Aires | 1.37 | 333,331 | 5 | 3 | - | - | 60 | measured |
| 295 | Thessaloniki | 1.42 | 180,145 | 4 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 296 | Ljubljana | 1.37 | 125,046 | 4 | - | 1 | - | 30 | measured |
| 297 | Vancouver | 1.37 | 351,552 | 7 | - | - | - | 30 | measured |
| 298 | Belgrade | 1.37 | 178,116 | 5 | 5 | - | - | 60 | measured |
| 299 | Brighton | 1.37 | 114,108 | 9 | 4 | 1 | - | 20 | measured |
| 300 | Manchester | 1.37 | 316,438 | 5 | 1 | - | - | 30 | measured |
| 301 | Nantes | 1.37 | 67,689 | 1 | 1 | - | - | 30 | measured |
| 302 | Nice | 1.37 | 136,877 | 10 | 6 | 2 | - | 30 | measured |
| 303 | York | 1.37 | 118,066 | 6 | 2 | 1 | - | 20 | measured |
| 304 | Sapporo | 0.88 | 88,633 | 6 | 1 | - | - | 60 | published, never ranked (may be uncrawled) |
| 305 | Antalya | 1.31 | 70,688 | - | - | - | - | 60 | predicted (travel demand) |
| 306 | Cardiff | 1.27 | - | 13 | 1 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 307 | Santa Fe | 1.29 | - | 3 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 308 | Breda | 0.64 | 36,579 | 11 | 1 | 2 | 120 | 20 | published, never ranked (may be uncrawled) |
| 309 | Colmar | 1.28 | 45,517 | - | - | - | - | 20 | predicted (travel demand) |
| 310 | Bodrum | 1.26 | 33,918 | - | - | - | - | 20 | predicted (travel demand) |
| 311 | Riga | 1.23 | 108,918 | 5 | 2 | - | - | 30 | published, never ranked (may be uncrawled) |
| 312 | Nafplio | 1.24 | 31,193 | - | - | - | - | 10 | predicted (travel demand) |
| 313 | Lausanne | 1.23 | 68,242 | 8 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 314 | Evora | 0.78 | 15,345 | - | - | - | - | 20 | predicted (travel demand) |
| 315 | Bergamo | 0.57 | 52,933 | 9 | 2 | 1 | 17 | 20 | published, never ranked (may be uncrawled) |
| 316 | Zaragoza | 0.73 | 87,580 | 7 | - | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 317 | Toulouse | 0.73 | 112,721 | 10 | - | 1 | 34 | 30 | published, never ranked (may be uncrawled) |
| 318 | Okinawa | 0.71 | 24,466 | 6 | - | - | 1 | 30 | published, never ranked (may be uncrawled) |
| 319 | Apeldoorn | 0.53 | - | 8 | - | 2 | 80 | 20 | published, never ranked (may be uncrawled) |
| 320 | Dubrovnik | 0.99 | 119,586 | 4 | 4 | - | 2 | 10 | published, never ranked (may be uncrawled) |
| 321 | Belfast | 1.04 | 224,315 | 8 | 3 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 322 | Split | 0.97 | 132,399 | 5 | - | 1 | 2 | 20 | published, never ranked (may be uncrawled) |
| 323 | Haarlem | 0.50 | 33,960 | 21 | 2 | 2 | 277 | 20 | published, never ranked (may be uncrawled) |
| 324 | Azores | 0.65 | - | 7 | 4 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 325 | Sorrento | 0.49 | 40,049 | 7 | - | 1 | 20 | 10 | published, never ranked (may be uncrawled) |
| 326 | Catania | 0.57 | 58,252 | 4 | 3 | 1 | 5 | 30 | published, never ranked (may be uncrawled) |
| 327 | Oaxaca | 0.95 | 72,955 | - | - | - | - | 60 | predicted (travel demand) |
| 328 | Innsbruck | 0.63 | 58,742 | 6 | 2 | 1 | 39 | 20 | published, never ranked (may be uncrawled) |
| 329 | Arnhem | 0.46 | 31,478 | 32 | 3 | 3 | 202 | 20 | published, never ranked (may be uncrawled) |
| 330 | Lucca | 0.45 | 52,271 | 16 | 4 | 1 | 27 | 20 | published, never ranked (may be uncrawled) |
| 331 | Kotor | 0.86 | 48,982 | 1 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 332 | Busan | 0.83 | 94,737 | 2 | - | - | - | 60 | published, never ranked (may be uncrawled) |
| 333 | Kandy | 0.78 | 24,159 | 1 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 334 | Bath | 0.77 | 144,950 | 9 | 2 | 2 | - | 20 | published, never ranked (may be uncrawled) |
| 335 | Potsdam | 0.51 | 51,727 | 18 | 9 | 3 | 16 | 20 | published, never ranked (may be uncrawled) |
| 336 | Enschede | 0.38 | - | 13 | 1 | 1 | 82 | 20 | published, never ranked (may be uncrawled) |
| 337 | Trento | 0.38 | 56,455 | 10 | 2 | 1 | 20 | 20 | published, never ranked (may be uncrawled) |
| 338 | Heidelberg | 0.67 | 75,837 | 7 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 339 | Modena | 0.44 | 51,698 | 5 | 1 | 1 | 3 | 20 | published, never ranked (may be uncrawled) |
| 340 | Den Bosch | 0.36 | 39,682 | 11 | 2 | 1 | 118 | 20 | published, never ranked (may be uncrawled) |
| 341 | Sao Paulo | 0.68 | 911 | 1 | - | - | - | 100 | measured |
| 342 | Assen | 0.35 | - | 9 | - | 2 | 66 | 20 | published, never ranked (may be uncrawled) |
| 343 | Heerlen | 0.35 | - | 8 | 1 | 2 | 53 | 20 | published, never ranked (may be uncrawled) |
| 344 | Kamakura | 0.44 | 33,492 | 7 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 345 | Zwolle | 0.35 | - | 15 | - | 3 | 58 | 20 | published, never ranked (may be uncrawled) |
| 346 | Inverness | 0.69 | 92,195 | 1 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 347 | Corfu | 0.68 | 139,334 | 8 | - | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 348 | Gran Canaria | 0.42 | - | 10 | 4 | 1 | - | 30 | published, never ranked (may be uncrawled) |
| 349 | Hallstatt | 0.50 | 47,271 | 7 | 4 | - | 4 | 10 | published, never ranked (may be uncrawled) |
| 350 | Tarragona | 0.36 | 32,396 | 3 | 1 | - | - | 20 | published, never ranked (may be uncrawled) |
| 351 | Hoorn | 0.30 | - | 12 | - | 2 | 52 | 20 | published, never ranked (may be uncrawled) |
| 352 | Lima | 0.51 | 132,792 | 5 | 1 | 1 | - | 100 | published, never ranked (may be uncrawled) |
| 353 | Rouen | 0.54 | 72,334 | 12 | - | 1 | 6 | 20 | published, never ranked (may be uncrawled) |
| 354 | Pamplona | 0.34 | 128,065 | 25 | 1 | 3 | 9 | 20 | published, never ranked (may be uncrawled) |
| 355 | Perugia | 0.29 | 42,572 | 16 | 1 | 2 | 19 | 20 | published, never ranked (may be uncrawled) |
| 356 | Phoenix | 0.55 | - | - | - | - | - | 60 | predicted (travel demand) |
| 357 | Roosendaal | 0.26 | - | 20 | - | 2 | 138 | 20 | published, never ranked (may be uncrawled) |
| 358 | Leuven | 0.51 | 40,645 | 4 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 359 | Killarney | 0.30 | 28,763 | 1 | 1 | - | - | 10 | published, never ranked (may be uncrawled) |
| 360 | Yakushima | 0.28 | - | 2 | 2 | - | 1 | 10 | published, never ranked (may be uncrawled) |
| 361 | Matera | 0.25 | 67,033 | 4 | - | - | 2 | 20 | published, never ranked (may be uncrawled) |
| 362 | Canterbury | 0.40 | 53,301 | 4 | 1 | 1 | - | 20 | published, never ranked (may be uncrawled) |
| 363 | Zadar | 0.38 | 71,549 | 1 | - | - | 1 | 20 | published, never ranked (may be uncrawled) |
| 364 | Toledo | 0.24 | 3,149 | - | - | - | - | 20 | predicted (travel demand) |
| 365 | Setubal | 0.19 | 22,582 | 10 | 4 | 2 | 13 | 20 | published, never ranked (may be uncrawled) |
| 366 | Anuradhapura | 0.32 | - | 1 | - | - | - | 20 | published, never ranked (may be uncrawled) |
| 367 | Regensburg | 0.30 | 51,930 | 8 | 2 | 1 | 3 | 20 | published, never ranked (may be uncrawled) |
| 368 | Bamberg | 0.24 | 28,716 | 11 | 7 | 1 | 15 | 20 | published, never ranked (may be uncrawled) |
| 369 | Newark | 0.29 | - | - | - | - | - | 10 | predicted (travel demand) |
| 370 | Assisi | 0.17 | 30,278 | 6 | 1 | 2 | 6 | 10 | published, never ranked (may be uncrawled) |
| 371 | Stratford-upon-Avon | 0.27 | 68,555 | 2 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 372 | La Palma | 0.17 | - | 4 | 3 | - | - | 20 | published, never ranked (may be uncrawled) |
| 373 | Allentown | 0.24 | - | 1 | - | - | 3 | 20 | predicted (travel demand) |
| 374 | Oss | 0.11 | - | 5 | - | - | 48 | 20 | published, never ranked (may be uncrawled) |
| 375 | Queenstown | 0.16 | 36,672 | - | - | - | - | 10 | predicted (travel demand) |
| 376 | San Juan | 0.15 | - | - | - | - | - | 10 | predicted (travel demand) |
| 377 | Windsor | 0.13 | 30,452 | 2 | - | - | - | 10 | published, never ranked (may be uncrawled) |
| 378 | Halifax | 0.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 379 | Memphis | 0.08 | - | - | - | - | - | 30 | predicted (travel demand) |
| 380 | George Town | 0.07 | 36,080 | 1 | - | - | - | 30 | published, never ranked (may be uncrawled) |
| 381 | Buffalo | 0.04 | - | 1 | - | - | - | 10 | published, never ranked (may be uncrawled) |

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

