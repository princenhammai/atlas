# Merge the two JSON parts

`entries.json` has rows 1–20. `entries.part2.json` has rows 21–39.

Until an AI pass concatenates them, merge locally:

```bash
python3 - <<'PY'
import json
from pathlib import Path
a = json.loads(Path('data/entries.json').read_text())
b = json.loads(Path('data/entries.part2.json').read_text())
seen = {e['id'] for e in a}
for e in b:
    if e['id'] not in seen:
        a.append(e)
Path('data/entries.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(len(a), 'entries')
PY
```

Then delete `data/entries.part2.json` and `data/MERGE.md`.

`python3 scripts/render_vault.py` rebuilds the markdown views from the merged JSON.
