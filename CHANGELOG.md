# Changelog

## 2026-09-22 — make the database usable

What was wrong:

- `data/entries.json` and `vault/` had already drifted.
- `vault/viet-nam/ha-noi/eat.md` was a category-count placeholder with no entries.
- Restaurant / drink / Đà Nẵng extras existed in markdown only.
- Fields were optional and inconsistent (`price` vs `price_hint`, missing tags/notes).
- No way to ask "what should I do in Đà Nẵng this week?"

What changed:

- JSON is canonical. Every row now has the full field set.
- Added `priority` (`next` / `someday` / `parked`), `context`, `maps`, `updated`.
- Recovered named Hà Nội eat entries from Threads sources already cited in the repo.
- Regenerated lane markdown from JSON so the two copies match.
- Added `vault/INDEX.md`, `vault/_next.md`, and a Đà Nẵng home-city card.
- Bakery names that were counted but never written stay in `_inbox` instead of a fake TOC.

Not done (needs you):

- Paste bakery carousel text / screenshots to file the 19 claimed tiệm bánh.
- Add a source URL for `Cơm Bắc Tầm Vị` (skip with no link).
- File real Đà Nẵng eat / drink / do / stay — those lanes are still empty.
