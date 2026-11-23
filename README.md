# Toilet Tales

A scrollytelling map and data story about the public toilets of Chepauk–Triplicane, Chennai.

During a research fellowship (July–December 2022), about 1,100 public toilets were surveyed across Chennai, and a baseline WASH (water, sanitation and hygiene) score was devised for them. Chepauk–Triplicane is the sample area shown here: 47 public toilets, 24 of which were scored on 25 indicators, each rated green (2), yellow (1) or red (0).

**Partners:** Greater Chennai Corporation, Recycle Bin, Toilet Tales, Cheer NGO, IHE Delft (Netherlands) and Madras Medical College.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The finished site. Open it in a browser, or serve it with GitHub Pages. |
| `template.html` | The page source, with placeholders for the data. Edit this one. |
| `build.py` | Combines `template.html` with the two data files into `index.html`. |
| `data.json` | The 47 toilets (name, status, coordinates) and the scores and criteria for the 25 indicators. |
| `roads.json` | Streets, rail, river and coastline for the map, simplified from OpenStreetMap. |

## Rebuilding

After changing `template.html` or the data, run:

```bash
python3 build.py
```

`build.py` writes the page body to `index.html` without the `<!doctype>`/`<head>` wrapper. For a standalone page, keep the wrapper at the top and bottom of the current `index.html`.

## Method

Each indicator is rated 0, 1 or 2, so the 25 indicators give a maximum of 50 points. The overall score is that total doubled, out of 100. The core score uses the 10 core indicators (maximum 20 points). The scoring tool was adapted from the WHO WASH FIT tool.

## Credits

Map data © OpenStreetMap contributors, available under the Open Database Licence (ODbL).
