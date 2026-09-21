# Schema

## Entry (markdown)

```md
## {Title}

- id: `{city-slug}-{short-slug}`
- status: want | been | skip
- lane: eat | drink | restaurant | play | do | stay | see | shop
- category: {short type}
- city: {city}
- country: {country}
- area: {district or empty}
- location: {address or empty}
- price: {hint or empty}
- tags: tag-one, tag-two
- sources:
  - {url or source title}
- notes: {why saved}
- caveats: {warnings, corrections, seasonal}
```

## Entry (JSON)

`data/entries.json` is an array of objects:

```json
{
  "id": "ha-noi-pho-ly-quoc-su",
  "title": "Phở Lý Quốc Sư",
  "status": "want",
  "lane": "eat",
  "category": "Phở",
  "city": "Hà Nội",
  "country": "Việt Nam",
  "area": "Hoàn Kiếm",
  "location": "27B Phùng Hưng",
  "price": "",
  "tags": [],
  "sources": ["https://www.threads.com/@tusuyen.vibe/post/DcwJqWHEuXb"],
  "notes": "Classic old-quarter phở.",
  "caveats": "",
  "added": "2026-09-22"
}
```

## File map

| path | contents |
|---|---|
| `vault/_inbox.md` | unnamed or unlocated dumps |
| `vault/{country}/{city}/eat.md` | food stalls and dishes |
| `vault/{country}/{city}/drink.md` | cafes, bars, tea |
| `vault/{country}/{city}/restaurant.md` | sit-down dining |
| `vault/{country}/{city}/play.md` | fun |
| `vault/{country}/{city}/do.md` | activities / skills |
| `vault/{country}/{city}/stay.md` | beds |
| `vault/{country}/{city}/see.md` | sights |
| `vault/{country}/{city}/shop.md` | markets and stores |

One lane per file. Create empty files only when the first real entry arrives.

## Rules

1. Never invent an address.
2. Never overwrite `been` or `skip` with `want`.
3. Merge on name + city, not on vibe.
4. Sources are mandatory. An entry with no source goes to `_inbox`.
5. Original-language titles stay original.
