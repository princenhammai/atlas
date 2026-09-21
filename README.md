# Atlas

Open personal field atlas — a living encyclopedia of **places to go and things to do**.

Not a social feed. Not a ratings app. A filing cabinet:

- eat · drink · restaurant · play · do · stay · see · shop
- any city, any country
- every entry keeps its **source**
- status is a checklist: `want` → `been` → `skip`

## How it works

1. Paste links, screenshots, or captions into any AI that can read this repo.
2. Paste [PROMPT.md](./PROMPT.md) as the system / standing instruction.
3. The AI extracts named places, drops chatter, merges duplicates, and commits into `vault/` + `data/entries.json`.

No app required. Git is the database.

## Layout

```text
PROMPT.md                         standing instruction for any AI
SCHEMA.md                         fields, lanes, file rules
vault/_inbox.md                   unsorted dumps
vault/{country}/{city}/{lane}.md  human-readable lists
data/entries.json                 machine index
```

## Status

| status | meaning |
|---|---|
| `want` | on the list, not checked yet |
| `been` | went / did it |
| `skip` | ignore, or local said don't |

## Seed

First dump is a Hà Nội foodtour filed from five Threads posts, plus a few public Đà Nẵng / Hội An landmarks so the non-food lanes exist.

## License

MIT. The schema and prompt are reusable. The entries are a personal field notebook — treat them as notes, not gospel.
