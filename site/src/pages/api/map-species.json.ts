// The species chip's list for a map that does not carry it inline (the city
// map, 2026-11-01): the names and their Latin as HTML, in the order and with
// the indexes /explore and /api/pins.json use (lib/map-species.ts).
import { mapSpecies } from "../../lib/map-species";
import { speciesIconKey } from "../../lib/species-icons";

export async function GET() {
  const { list, latinHtml } = await mapSpecies();
  // icons: the drawing on each species' map pin (tree-pins-js.ts), so the
  // city map draws its neighbours' trees with the same pin as its own.
  return new Response(JSON.stringify({ names: list, latin: latinHtml, icons: list.map((s) => speciesIconKey(s)) }),
                      { headers: { "Content-Type": "application/json" } });
}
