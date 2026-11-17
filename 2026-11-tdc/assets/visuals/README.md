# Local teaching visuals

## Current direction: quantitative comparison

Open `preview/renal-excretion-comparison.png` for the 32-medicine overview. Three `renal-excretion-` group charts provide 16:9 slide exports, and `renal-excretion-comparators-denominators.png` shows gabapentin, metformin and digoxin separately. SVG and PDF versions are in `source/`. See `renal-excretion-sources.md` and the matching JSON/CSV for per-drug evidence, numerator/denominator notes and limitations. Rebuild with `build_renal_excretion.py` and matplotlib.

## Earlier conceptual drafts

Six original editable SVGs and 2400 × 1350 PNG previews for the priority slides in VISUAL_PLAN.md. These are local review assets; no R2 upload or lesson changes have been made. File mappings and proposed alt text are in `manifest.json`.

All artwork is constructed from original SVG shapes and text. No external image assets were copied or adapted, so no Servier attribution is required. Text remains editable. PNGs use a white background. Clinical diagrams are schematic, not to scale.

## Evidence and review

- **Slide 2:** existing lesson, `three-issues`; conceptual illustration without measured data.
- **Slide 9:** [Davis et al., 2018](https://doi.org/10.1186/s12882-018-1101-4). Original simplified mechanism diagram; no published figure reproduced.
- **Slide 12:** [Medsafe lithium interactions, 2017](https://www.medsafe.govt.nz/profs/PUArticles/September2017/Lithium.htm) and [SGLT2 inhibitor interaction, 2023](https://www.medsafe.govt.nz/profs/PUArticles/March2023/Starting-empagliflozin-or-dapagliflozin-in-patients-on-lithium.html). Qualitative arrows; no comparative effect sizes. Selected classes from the lesson, not an exhaustive interaction list.
- **Slide 14 — review draft:** literal transcription of the existing `gaba-dosing` table. Australian formulation-specific PI and full haemodialysis regimens still need verification before clinical teaching or publication. CrCl has not been relabelled as eGFR. Independent linear scales are used for each medicine; marked segments show ranges rather than recommended starting doses.
- **Slide 17:** existing lesson, `polypharmacy`; qualitative diagram, no estimated risk score.
- **Slide 18:** [BC Transplant medication guidelines](https://www.transplant.bc.ca/Documents/Statistics/Clinical%20Guidelines%20for%20Transplant%20Medications.pdf) and existing `tx-mechanism` table. Focuses on CYP3A4 metabolism; does not depict the separate P-glycoprotein pathway or quantify effects.

## Regeneration

Use Python with `cairosvg` installed, then run `python3 assets/visuals/build_visuals.py` from the project directory. The script reads slide 14 values from `lesson.json`.

Review the PNGs locally before uploading to `fimbria-teaching-assets/tdc-2026/`. Set Fimbria image URLs only after public delivery URLs are confirmed.
