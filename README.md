# Atlas

Open personal field atlas — a living encyclopedia of **places to go and things to do**.

Not a social feed. Not a ratings app. A filing cabinet:

- eat · drink · restaurant · play · do · stay · see · shop
- any city, any country
- every entry keeps its **source**
- status is a checklist: `want` → `been` → `skip`
- priority is a queue: `next` → `someday` → `parked`

Git is the database. JSON is the source of truth. Markdown is the readable copy.

## How it works

1. Paste links, screenshots, or captions into any AI that can read this repo.
2. Paste [PROMPT.md](./PROMPT.md) as the standing instruction.
3. The AI extracts named places, drops chatter, merges duplicates, and writes `data/entries.json` first, then the matching `vault/` files.

## Layout

```text
PROMPT.md                         standing instruction for any AI
SCHEMA.md                         fields, lanes, file rules
CHANGELOG.md                      what changed in the system
scripts/render_vault.py           rebuild vault views from JSON
data/entries.json                 CANONICAL index
vault/INDEX.md                    generated city / count table
vault/_next.md                    generated next-up list
vault/_inbox.md                   unsorted dumps
vault/{country}/{city}/{lane}.md  human-readable lists
vault/viet-nam/da-nang/README.md  home-city card
```

## Status

| status | meaning |
|---|---|
| `want` | on the list, not checked yet |
| `been` | went / did it |
| `skip` | ignore, or local said don't |

## Priority

| priority | meaning |
|---|---|
| `next` | do this soon (weekend / next trip) |
| `someday` | filed, no date |
| `parked` | keep the note, do not surface in next-up |

## Home city

Đà Nẵng is home base. Travel lists (Hà Nội, Hội An, elsewhere) stay in the same schema with `context: travel`.

## Seed

Hà Nội foodtour recovered from Threads posts already in the repo, plus public Đà Nẵng / Hội An landmarks so non-food lanes exist. Bakery names that never got bodies stay in `_inbox`.

## License

MIT. The schema and prompt are reusable. The entries are a personal field notebook — treat them as notes, not gospel.
