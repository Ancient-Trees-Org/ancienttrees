// READERS' NOTES IN THE BUILT PAGE (Hidde, 2026-11-27: "Ja, bouw 1 en 2").
// TREE_NOTES_JS used to be the only way a note reached a tree page, so the
// HTML a crawler got held the empty card and never the words. The build now
// writes the notes in, from data/build/tree-notes.json (scripts/
// notes_for_build.py, deploy.yml, gitignored: readers' words never live in
// the repository). The script still redraws the block from Supabase on load,
// so a note written after the build shows at once and a hidden one goes.
// Missing file: no notes, the empty card, exactly as before.
import fs from "node:fs";
import path from "node:path";
import { DATA } from "./data-dir";

export type BuiltNote = { body: string; created_at: string | null; author_name: string | null };

let cached: Record<string, BuiltNote[]> | null = null;

function load(): Record<string, BuiltNote[]> {
  if (cached) return cached;
  try {
    const doc = JSON.parse(fs.readFileSync(path.join(DATA, "build", "tree-notes.json"), "utf-8"));
    cached = doc.notes ?? {};
  } catch {
    cached = {};
  }
  return cached!;
}

/** The visible notes on this tree, newest first; [] when none or no file. */
export function builtNotes(treeId: string): BuiltNote[] {
  return load()[treeId] ?? [];
}

/** The newest note's day (YYYY-MM-DD), for the page's lastmod; null when none. */
export function newestNoteDay(treeId: string): string | null {
  const n = builtNotes(treeId)[0];
  return n && n.created_at ? n.created_at.slice(0, 10) : null;
}

/** The day as the script writes it (toLocaleDateString, day numeric, month
 *  short, year numeric), so the built page and the redrawn one agree. */
export function noteDay(iso: string | null, lang: string): string {
  if (!iso) return "";
  try {
    return new Date(iso).toLocaleDateString(lang, { day: "numeric", month: "short", year: "numeric" });
  } catch {
    return "";
  }
}
