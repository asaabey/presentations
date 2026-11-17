# Visual plan for psychiatric pharmacotherapy in kidney disease

Suggestions for the revised 29-slide lesson. Slide numbers below refer to the current lesson.json. Prioritise six additions: slides 2, 9, 12, 14, 17 and 18. These explain mechanisms and prescribing decisions without adding more transplant content. The deck itself has not been changed.

## Revised direction: quantitative renal elimination comparison

The user prefers a sourced, drug-by-drug percentage graph over the initial conceptual diagrams. Local assets now include `renal-excretion-comparison.png`, three medicine-group charts and a separate comparator-denominator chart in `assets/visuals/preview/`, with editable SVGs and PDFs in `assets/visuals/source/`. The data cover 32 medicines. Per-drug evidence and limitations are in `assets/visuals/renal-excretion-sources.md`; values are available as JSON and CSV.

The common plotted metric is percentage of administered dose recovered unchanged in urine. This is not identical to the renal fraction of total systemic clearance. Gabapentin and metformin use absorbed-drug denominators, and digoxin uses an IV-dose denominator, so their values have a separate chart. Parent-drug recovery does not capture active-metabolite accumulation or establish safety in CKD. Existing conceptual assets remain available as earlier drafts. No lesson changes or R2 upload yet.

## Original recommended visuals

| Slide | Suggested visual and composition | Image or evidence source | Production notes |
|---|---|---|---|
| 2 — Three different questions | Three-panel diagram: kidney clearance, drug accumulation in the bloodstream, and direct kidney injury. Use the same medicine icon throughout, with separate arrows for each process. | Original illustration; kidney and circulation components from [Servier Medical Art](https://smart.servier.com/). | Label panels Clearance, Accumulation and Nephrotoxicity. Avoid implying that accumulation always damages the kidney. This establishes a visual vocabulary for later slides. |
| 4 — Antidepressants in CKD | Convert the dense table into three groups: little routine renal adjustment, reduced clearance requiring dose changes, and additional cautions. Keep drug names visible. | Existing lesson table; verify individual entries against Australian product information before artwork is finalised. [TGA medicine information](https://www.tga.gov.au/products/medicines/find-information-about-medicine). | Original editable diagram. Do not use a single green-to-red safety ranking: renal clearance, QT effects and sedation are different issues. Retain dosing details in notes or a handout. |
| 5 — Duloxetine | Horizontal kidney-function band with eGFR 30 marked; enlarge the advanced CKD region and add a separate small callout for formulation-specific Australian advice. | [NIDDK drug dosing guidance](https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/ckd-drug-dosing-providers); Australian brand-specific PI. | Original illustration. A decision aid, not a measured dose-response graph. Show eGFR units. Do not suggest that reported eGFR and label-based creatinine clearance are universally interchangeable. |
| 7 — SSRI adverse effects | Four labelled icons: sodium/water balance, QT interval, serotonin toxicity and falls. Use one short risk cue beneath each. | Original icons or adapted Servier components; clinical content from the existing slide. | No bleeding-risk icon. A schematic ECG can illustrate a prolonged QT interval; label it schematic and avoid diagnostic measurements. |
| 9 — Lithium and the kidney | Simplified nephron with an enlarged collecting duct. Show lithium entry, impaired water reabsorption and increased urine output; add a separate chronic interstitial injury inset. | [Davis et al., lithium and nephrotoxicity](https://doi.org/10.1186/s12882-018-1101-4); nephron components from Servier. | Original mechanism drawing. Keep acute water-handling effects distinct from chronic structural injury. Avoid reproducing a complex histology figure unless it supports a specific teaching point. |
| 10 — Lithium monitoring | Circular calendar with lithium, eGFR/electrolytes, calcium and thyroid monitoring; a side arrow leads to earlier review during illness or medication changes. | Existing slide and [Davis et al.](https://doi.org/10.1186/s12882-018-1101-4). | Original workflow diagram. Show routine monitoring and additional clinically triggered checks separately; do not imply everyone has an identical schedule. |
| 12 — Drugs that move lithium levels | Directional interaction map: lithium in the centre; upward arrows from thiazides, ACE inhibitors/ARBs and NSAIDs; downward arrow from SGLT2 inhibitors; neutral marker for amlodipine. | Existing interaction table; confirm mechanisms and current warnings before final production. | Use qualitative arrows of equal size. Arrow lengths must not imply comparative effect sizes. Put the monitoring action beneath the diagram. |
| 14 — Gabapentinoid dosing | Two aligned dose-range charts by kidney-function category, one for each drug; place dialysis dosing in a separate strip. | Existing dosing table, checked against the specific Australian formulations. | Use separate drug scales and labelled ranges, not a continuous interpolated curve. Preserve the kidney-function metric used by the underlying dosing source. Never relabel a CrCl-derived table as eGFR without reviewing the conversion. |
| 16 — Antipsychotics and sedatives | Matrix with columns for renal accumulation, sedation/orthostasis, QT and metabolic effects. Place named medicines in rows. | Existing slide table; product-specific verification needed for any new matrix cells. | A proposed editorial layout, not a validated risk score. Leave unsupported comparisons blank rather than assigning invented severity ratings. |
| 17 — Stacking risk in dialysis | Converging arrows from QT-prolonging medicines and electrolyte shifts into a central cardiac electrical-risk icon; finish with ECG and electrolyte review. | Existing slide; original illustration using heart/ECG components from Servier. | Use a qualitative diagram. Avoid additive numerical scores or proportional bars: this slide has no quantitative risk model. |
| 18 — Calcineurin inhibitor interactions | Two parallel lanes: inhibitor → reduced metabolism → higher exposure → toxicity; inducer → increased metabolism → lower exposure → rejection risk. Add a small reversal arrow for stopping the interacting medicine. | [BC Transplant medication guidelines](https://www.transplant.bc.ca/Documents/Statistics/Clinical%20Guidelines%20for%20Transplant%20Medications.pdf). | Highest-priority transplant visual. Replace the current mechanism table rather than adding another transplant slide. Use a generic inhibitor; do not depict fluoxetine as a uniformly strong CYP3A4 inhibitor. |
| 22 — Interaction summary | Compact arrow-labelled medicine cards grouped by potential higher CNI exposure, lower exposure and other concerns such as QT/sedation. | BC Transplant guidelines above; existing table. | Reuse slide 18 icons. Keep potential exposure effects distinct from QT and sedation concerns. This is optional if the table remains readable. |
| 23 — Practical actions | Four-step flow: identify medication change → contact transplant team → arrange agreed monitoring → reassess after starting or stopping. | BC Transplant guidelines above; existing slide. | Original workflow. Avoid a universal timing axis; monitoring depends on the interacting drug and transplant service plan. |
| 24 — Steroid psychiatric effects | Three-column chart of the historical dose categories already shown in the lesson. Start the percentage axis at zero and label each column directly. | Original study cited in the deck: Boston Collaborative Drug Surveillance Program, Clin Pharmacol Ther 1972;13:694–698. Locate the original report before extracting precise values. | Existing rounded values are about 1%, 5% and 18%. Verify exact percentages, category boundaries and outcome wording from the original before plotting. Title it Historical psychiatric reactions by prednisone dose; do not label the outcome psychosis alone or portray it as a transplant-specific prediction. |
| 27 — GP checklist | Three-stage prescribing pathway: before prescribing, after starting/changing, and urgent symptoms. Put lithium and transplant actions in small branches. | Existing checklist; original editable flowchart. | Keep this a practical summary. Avoid seven equally weighted icons with small labels. |
| 28 — Take-home messages | Five concise illustrated cards using icons already introduced: antidepressant, lithium, accumulation, interactions and urgent neurological symptoms. | Reuse the original diagrams above. | No new graph or statistic. Consistency makes the final summary easier to recall. |

## Optional graphs within case explanations

Use these after revealing the answer, so they do not give it away.

- **Slide 8, lithium decline case:** plot the two supplied eGFR observations, 78 and 46, ten years apart. Label them case values and connect with a dashed line; do not invent intermediate results or imply a measured linear trajectory.
- **Slide 13, pregabalin toxicity case:** paired schematic concentration curves for normal and reduced clearance under repeated dosing. Label the curves illustrative, with no numerical concentration scale or invented toxicity threshold. The purpose is accumulation, not estimating this patient's concentration.
- **Slide 20, carbamazepine case:** a qualitative timeline showing medication initiation followed by falling tacrolimus exposure and concern for rejection. Do not invent measured tacrolimus values or present rejection as confirmed by the creatinine rise alone.

## Image sourcing and attribution

**Preferred reusable anatomy source:** [Servier Medical Art](https://smart.servier.com/). Its [terms of use](https://smart.servier.com/terms-of-use/) specify CC BY 4.0. Search within the library for kidney, nephron, collecting duct, blood vessel, heart and brain. Select the exact asset before recording its download link and attribution.

Suggested credit: “Adapted from Servier Medical Art, CC BY 4.0” with links to the original asset and licence. Record modifications such as recolouring, cropping or added arrows.

**Published figures:** use the paper as evidence and create a fresh explanatory diagram where practical. Check the individual figure credit and licence before reuse; an open-access article can contain third-party images with separate rights. Avoid screenshots of drug handbooks and dosing tables.

**Original illustrations:** create editable SVG or slide-native shapes for arrows, timelines, medicine cards and graphs. AI-generated artwork is suitable for an optional decorative opening image; nephron anatomy, ECGs, drug doses and graphs should be constructed and checked explicitly.

## Build briefs for the first six assets

1. **Clearance versus accumulation versus injury:** three equal panels, white background, navy outlines, teal kidney, amber medicine dots, short labels, no decorative anatomy.
2. **Lithium nephron:** simplified nephron at left, collecting-duct inset at right, labelled lithium entry and reduced water reabsorption, separate chronic-injury inset, editable labels.
3. **Lithium interactions:** central lithium card with equally sized directional arrows, medicine classes around it, one monitoring action below, no invented percentages.
4. **Gabapentinoid dosing:** two aligned horizontal range plots, explicit units, source-based category labels, separate dialysis strip, every range checked against final source data.
5. **QT stacking:** three medicine cards and one electrolyte card converging on a heart/ECG symbol, followed by ECG and electrolyte review, no numeric risk score.
6. **CNI mechanism:** two horizontal lanes with the same four stages, clear up/down arrows, toxicity and rejection labelled explicitly, small stopping/reversal note.

Use navy text, teal for ordinary process flow, amber for caution and red for urgent harm. Pair every colour with a label or symbol. Keep one teaching message per visual, use large labels, and export both an editable source and a high-resolution preview. Put evidence citations in a readable slide footer.

## Local assets and R2 delivery

Build and review assets locally first. Use `assets/visuals/source/` for editable SVGs and `assets/visuals/preview/` for high-resolution PNGs. Keep matching descriptive filenames in both folders:

| Slide | Filename stem |
|---|---|
| 2 | `clearance-accumulation-injury` |
| 9 | `lithium-nephron` |
| 12 | `lithium-interactions` |
| 14 | `gabapentinoid-dosing` |
| 17 | `qt-stacking` |
| 18 | `cni-interactions` |

Record evidence sources, attribution, modifications and proposed alt text in `assets/visuals/README.md` as assets are produced. Review anatomy, clinical labels and source-dependent doses before upload.

After local review, upload the delivery images using Wrangler to bucket `fimbria-teaching-assets`, under object prefix `tdc-2026/`. For example:

```bash
npx wrangler r2 object put fimbria-teaching-assets/tdc-2026/clearance-accumulation-injury.png --file assets/visuals/preview/clearance-accumulation-injury.png --content-type image/png --remote
```

The supplied S3 storage address is `https://6ae10ac17c868ab792e4b1877d7a1ccf.r2.cloudflarestorage.com/fimbria-teaching-assets`. Confirm a public delivery base URL (custom domain or R2 public URL) before wiring images into the lesson; the S3 API endpoint is separate from public bucket delivery. See [Cloudflare public bucket documentation](https://developers.cloudflare.com/r2/buckets/public-buckets/).

The [Fimbria lesson schema](https://fimbria.lattice-1.com/lesson.schema.json) was checked against the local `lesson.schema.json` and matches. Each slide or question supports one `image` object with required `src` and `alt`, and optional `caption` (maximum lengths: 2048, 500 and 300 characters respectively). Compose multi-panel visuals into a single image. Set `src` to the final hosted asset URL after upload and verify that it loads publicly.

Add image references through `build.py`, which generates `lesson.json`, so rebuilding preserves them. Keep the lesson unchanged until assets and delivery URLs are ready.
