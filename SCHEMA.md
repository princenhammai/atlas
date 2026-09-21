# Schema

`data/entries.json` is canonical. Vault markdown is a readable projection of the same objects. If they disagree, JSON wins — then regenerate or rewrite the markdown to match.

## Entry (JSON)

`data/entries.json` is an array of objects. Every object uses this full shape. Empty string / empty array when unknown. Never omit keys.

```json
{
  "id": "ha-noi-pho-ly-quoc-su",
  "title": "Phở Lý Quốc Sư",
  "status": "want",
  "priority": "someday",
  "lane": "eat",
  "category": "Phở",
  "city": "Hà Nội",
  "country": "Việt Nam",
  "area": "Hoàn Kiếm",
  "location": "27B Phùng Hưng",
  "maps": "Phở Lý Quốc Sư, 27B Phùng Hưng, Hà Nội",
  "price": "",
  "tags": [],
  "context": ["travel"],
  "sources": ["https://www.threads.com/@tusuyen.vibe/post/DcwJqWHEuXb"],
  "notes": "Classic old-quarter phở.",
  "caveats": "",
  "added": "2026-09-22",
  "updated": "2026-09-22"
}
```

## Entry (markdown)

```md
## {Title}

- id: `{city-slug}-{short-slug}`
- status: want | been | skip
- priority: next | someday | parked
- lane: eat | drink | restaurant | play | do | stay | see | shop
- category: {short type}
- city: {city}
- country: {country}
- area: {district or empty}
- location: {address or empty}
- maps: {search string or empty}
- price: {hint or empty}
- tags: tag-one, tag-two
- context: home, travel, date, solo, guest, content, skill
- sources:
  - {url or source title}
- notes: {why saved}
- caveats: {warnings, corrections, seasonal}
- added: YYYY-MM-DD
- updated: YYYY-MM-DD
```

## Fields

| field | rule |
|---|---|
| `id` | `{city-slug}-{short-slug}`. Stable. Never mint a second id for the same venue+city. |
| `title` | Original-language name. Do not translate proper nouns. |
| `status` | `want` default. Never overwrite `been` or `skip` with `want`. |
| `priority` | `next` / `someday` / `parked`. Default `someday`. |
| `lane` | one of the eight lanes |
| `category` | short type inside the lane |
| `area` | district / neighborhood if known |
| `location` | street address if known. Empty beats a guess. |
| `maps` | pasteable search string built only from known title/address/city |
| `price` | only if the source stated it |
| `tags` | slugs: `seasonal`, `multi-source`, `local-disputed`, `queue`, `chain`, `date`, `home`, `night`, `strip`, `full-day`, `day-trip`, `address-corrected` |
| `context` | why it matters here: `home` `travel` `date` `solo` `guest` `content` `skill` |
| `sources` | mandatory. No source → `_inbox` |
| `added` / `updated` | ISO date |

Lane cheat sheet:

- `eat` — street food, specific dishes, casual stalls
- `drink` — cafe, bar, tea, wine, beer
- `restaurant` — sit-down dining, date-night, set menus
- `play` — beach, club, karaoke, amusement, sport for fun
- `do` — class, workshop, skill, quest, activity with intent
- `stay` — hotel, homestay, hostel
- `see` — landmark, museum, temple, viewpoint, old town
- `shop` — market, store, maker

## File map

| path | contents |
|---|---|
| `data/entries.json` | canonical array |
| `vault/INDEX.md` | generated counts |
| `vault/_next.md` | generated next-up |
| `vault/_inbox.md` | unnamed or unlocated dumps |
| `vault/{country}/{city}/{lane}.md` | one lane per file |
| `vault/viet-nam/da-nang/README.md` | home-city card |

Slugs: lowercase, hyphenated, ASCII-friendly (`viet-nam`, `ha-noi`, `da-nang`, `hoi-an`, `tokyo`, `new-york`).

Create a lane file only when the first real entry arrives. Never leave `PLACEHOLDER` as the body.

Sort entries in a file by category, then title.

## Rules

1. Never invent an address or coordinates.
2. Never overwrite `been` or `skip` with `want`.
3. Merge on name + city, not on vibe.
4. Sources are mandatory. An entry with no source goes to `_inbox` (the one inherited skip without a URL is flagged there).
5. Original-language titles stay original.
6. JSON first, markdown second, same fields.
7. Home city is Đà Nẵng. New local eat/drink/do/stay beats another travel landmark.
8. Do not add fields that are not in this file unless the user asks to change the schema.
