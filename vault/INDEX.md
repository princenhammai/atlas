# Atlas index

`data/entries.json` is canonical. This file is a generated view.

Total entries: **39**

| country | city | want | been | skip | next | files |
|---|---|---:|---:|---:|---:|---|
| Việt Nam | Hà Nội | 32 | 0 | 1 | 0 | [`eat.md`](./viet-nam/ha-noi/eat.md), [`drink.md`](./viet-nam/ha-noi/drink.md), [`restaurant.md`](./viet-nam/ha-noi/restaurant.md) |
| Việt Nam | Hội An | 1 | 0 | 0 | 0 | [`see.md`](./viet-nam/hoi-an/see.md) |
| Việt Nam | Đà Nẵng | 5 | 0 | 0 | 3 | [`play.md`](./viet-nam/da-nang/play.md), [`see.md`](./viet-nam/da-nang/see.md), [`shop.md`](./viet-nam/da-nang/shop.md) |

## Home city

Đà Nẵng is home base. Ask: *what's next in Đà Nẵng this week?*

## How to query

- `what's good in {city}` — read filed entries first
- `file this` + links — clerk extracts and upserts
- `mark {id} been` — status only, never overwrite been/skip with want
- `next in Đà Nẵng` — priority=next + context=home
