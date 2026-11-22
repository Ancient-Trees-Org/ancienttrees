// The trees that carry a visitor's photograph, for the bell's dropdown (Base.astro,
// lib/activity-js.ts, 2026-11-22): name, place, link, lead photo and each
// visitor photograph's own small copy, the same data the /visitors page and
// /activity bake in (lib/visitor-cards.ts). A few hundred trees, so the
// dropdown on any page asks for this and not for the 2 MB cards.json.
import type { APIRoute } from "astro";
import { visitorCards } from "../../lib/visitor-cards";

export const GET: APIRoute = async () =>
  new Response(JSON.stringify(await visitorCards("en")), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
