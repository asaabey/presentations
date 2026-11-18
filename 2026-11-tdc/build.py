#!/usr/bin/env python3
"""Build lesson.json (Fimbria lesson format, schemaVersion 1).

Edit the content here, then run:  python3 build.py
Format spec: https://fimbria.lattice-1.com/docs/lesson-format.md
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
steps = []


def slide(id, title, body, table=None):
    s = {"id": id, "type": "slide", "title": title, "body": body.strip("\n")}
    if table:
        s["table"] = table
    steps.append(s)


# Options are written with the correct answer first for readability; this
# fixed sequence decides where the correct answer is actually placed.
ANSWER_POSITIONS = [1, 3, 0, 2, 1, 0, 3, 2, 0, 1, 3, 2, 1, 0, 2, 3]


# Fimbria animates question prompts and revealed explanations directly.
# Keep to two effects per appearance and preserve the original MCQ wording.
QUESTION_EMPHASIS = {
    "q-ad-ckd4": (("CKD stage 4 (eGFR 22)", "moderate depression"),
                  ("hepatically metabolised", "no formal renal dose adjustment")),
    "q-ssri-na": (("sodium 121 mmol/L", "shortly after starting escitalopram while taking a thiazide"),
                  ("lower, though not zero, risk of hyponatraemia", "previous severe episode")),
    "q-li-decline": (("eGFR has fallen from 78 to 46 over 10 years", "4 L of urine a day"),
                     ("**lithium-associated CKD**", "**nephrogenic diabetes insipidus**")),
    "q-valproate-free": (("albumin 25 g/L", "total valproate concentration is within the laboratory therapeutic range"),
                        ("reduce valproate protein binding", "free fraction may rise")),
    "q-antipsych": (("CrCl 25 mL/min", "new oral antipsychotic"),
                   ("largely excreted unchanged by the kidney", "oral dose is reduced")),
    "q-insomnia": (("CrCl 24 mL/min", "severe, short-term insomnia"),
                  ("starting dose in renal impairment is 3.75 mg", "Review within a week")),
    "q-tx-cbz": (("starts carbamazepine", "Three weeks later"),
                ("**Carbamazepine is a strong enzyme inducer.**", "tacrolimus levels fall")),
    "q-memantine": (("CrCl is 22 mL/min", "immediate-release memantine"),
                   ("5 mg twice daily at CrCl 5–29 mL/min", "Do not routinely increase")),
    "q-acamprosate": (("CrCl 24 mL/min", "acamprosate to help maintain abstinence"),
                     ("renally eliminated", "contraindicated at CrCl ≤30 mL/min")),
    "q-case-hd": (("haemodialysis", "poor sleep, poor appetite and itch"),
                  ("helps sleep and appetite", "clearance is reduced")),
}


def underline_phrases(text, phrases):
    for phrase in phrases:
        if text.count(phrase) != 1 or "\n" in phrase:
            raise ValueError(f"Underline phrase must occur once on one line: {phrase!r}")
        text = text.replace(phrase, f"[underline]{phrase}[/underline]", 1)
    return text


def question(id, prompt, options, correct, explanation, table=None):
    clues, reasoning = QUESTION_EMPHASIS[id]
    prompt = underline_phrases(prompt, clues)
    explanation = underline_phrases(explanation, reasoning)
    options = list(options)
    n = sum(st["type"] == "question" for st in steps)
    pos = ANSWER_POSITIONS[n % len(ANSWER_POSITIONS)] % len(options)
    idx = next(i for i, (k, _) in enumerate(options) if k == correct)
    options.insert(pos, options.pop(idx))
    opts = [{"id": k, "text": v} for k, v in options]
    s = {
        "id": id,
        "type": "question",
        "prompt": prompt.strip("\n"),
        "options": opts,
        "correctOptionId": correct,
        "explanation": explanation.strip("\n"),
    }
    if table:
        s["table"] = table
    steps.append(s)


# ---------------------------------------------------------------- Opening
slide("intro", "Psychiatric pharmacotherapy in kidney disease and transplantation", """
A practical, case-based session for general practice.

By the end you should be able to:
1. Choose a reasonable first-line antidepressant in CKD stages 3–5, including dialysis
2. Recognise psychotropics that **accumulate** in renal impairment
3. Manage lithium safely, including during acute illness
4. Spot important psychotropic–immunosuppressant interactions
5. Ask: is this really a psychiatric illness?
""")

slide("three-issues", "Three different questions for every drug", """
1. **Clearance:** is it renally cleared? Does the dose need to change?
2. **Accumulation:** do active drug or metabolites build up and cause toxicity?
3. **Nephrotoxicity:** does it damage the kidney?

A drug can be completely non-nephrotoxic and still cause severe encephalopathy as kidney function falls.
""")

# ---------------------------------------------------------------- 1. Depression and anxiety in CKD

question("q-ad-ckd4", """
Margaret, 64, has type 2 diabetes and CKD stage 4 (eGFR 22). She has moderate depression and would like to try medication alongside counselling.

Which is the most reasonable first choice?
""", [
    ("sert", "Sertraline 25 mg daily, increasing to 50 mg"),
    ("desv", "Desvenlafaxine 100 mg daily"),
    ("dulox", "Duloxetine 60 mg daily"),
    ("ami", "Amitriptyline 25 mg at night"),
], "sert", """
**Sertraline** is hepatically metabolised, needs no formal renal dose adjustment, and has relatively low interaction potential, so it is a common first choice in advanced CKD. Start low and titrate slowly.

- **Desvenlafaxine** is largely renally cleared. At CrCl <30 the dose must be reduced substantially (no more than 50 mg every second day); 100 mg daily is too much.
- **Duloxetine** exposure rises markedly in severe renal impairment. Many guidelines advise avoiding it below CrCl 30, and 60 mg would be inappropriate here.
- **Amitriptyline** brings anticholinergic effects, orthostatic hypotension, falls and QT prolongation, all worse in CKD.

""")


slide("ad-table", "Antidepressants in CKD: the table to keep", "", table={
    "columns": ["Drug", "Renal considerations", "GP message"],
    "rowHeaders": True,
    "rows": [
        ["Sertraline", "No formal renal adjustment", "Often a useful first choice, including advanced CKD and dialysis"],
        ["Escitalopram", "Caution at CrCl <30", "Dose-related QT prolongation; check electrolytes and other QT drugs"],
        ["Fluoxetine", "Little renal adjustment", "Very long half-life; significant CYP interactions"],
        ["Venlafaxine", "Drug and active metabolite accumulate", "Reduce dose 25–50% in CKD; about 50% on dialysis"],
        ["Desvenlafaxine", "Mainly renally cleared", "CrCl <30 or dialysis: max 50 mg every second day"],
        ["Duloxetine", "Exposure rises at CrCl <30", "Generally avoid at CrCl <30; recommendations vary by formulation"],
        ["Mirtazapine", "Clearance falls 30–50%", "Start 7.5 mg; helps sleep and appetite; watch sedation and falls"],
        ["TCAs", "Metabolites accumulate", "Avoid for depression: anticholinergic, falls, QT"],
    ],
})

slide("duloxetine-nuance", "A note on duloxetine", """
- **eGFR <30 mL/min/1.73m²:** generally avoid duloxetine because exposure rises in severe renal impairment
- For some formulations, **30 mg daily** is recommended in severe renal impairment

Treat this as a formulation-specific prescribing decision, not a universal ban. If you use it, use the lowest dose and monitor closely.
""")

question("q-ssri-na", """
Joan, 79, has CKD stage 3b and persistent depression despite psychological treatment. Six months ago, she was admitted with confusion and sodium 121 mmol/L shortly after starting escitalopram while taking a thiazide. Both medicines were stopped, and her sodium returned to normal. Her current sodium is 138 mmol/L.

She would now like to try another antidepressant. Which is the most appropriate option given her previous adverse reaction?
""", [
    ("mirtazapine", "Mirtazapine"),
    ("sertraline", "Sertraline"),
    ("venlafaxine", "Venlafaxine"),
    ("escitalopram", "Escitalopram at a lower dose"),
], "mirtazapine", """
**Mirtazapine** is the most appropriate option here because it carries a lower, though not zero, risk of hyponatraemia than SSRIs and SNRIs. Her previous severe episode should influence the choice even though her sodium is now normal and the thiazide has been stopped.

- **Sertraline** has favourable renal dosing, but switching to another SSRI does not remove the risk of recurrent hyponatraemia.
- **Venlafaxine** also carries a risk of hyponatraemia and requires renal dose adjustment.
- **Escitalopram at a lower dose** re-exposes her to the suspected causative drug; a lower dose does not reliably prevent recurrence.

Mirtazapine clearance is reduced in CKD: start cautiously, titrate slowly, and monitor sedation and falls. Check sodium at baseline and early after starting treatment, with repeat monitoring guided by her risk and clinical course. New confusion or unsteadiness warrants prompt assessment and a sodium check.
""")

slide("ad-hyponatraemia", "Antidepressants: hyponatraemia risk", """
**Pooled event rates, not a ranking:** populations, follow-up and sodium thresholds varied substantially. These are not CKD-specific or annual risks; wide confidence intervals limit comparisons between individual drugs.

Direct comparisons support **lower risk with mirtazapine than SSRIs**, but risk is not zero (OR 0.61; 95% CI 0.39–0.96).

Source: [Gheysens T et al. European Psychiatry 2024;67:e20, Tables 3–4](https://doi.org/10.1192/j.eurpsy.2024.11). Any hyponatraemia: Na <135 mmol/L or a documented diagnosis; some studies only reported Na <130.
""", table={
    "columns": ["Agent", "Pooled event rate (95% CI)", "Studies"],
    "rowHeaders": True,
    "rows": [
        ["Sertraline", "4.59% (0.63–26.81%)", "7"],
        ["Escitalopram", "3.21% (0.33–24.86%)", "6"],
        ["Fluoxetine", "3.33% (1.09–9.71%)", "12"],
        ["Citalopram", "0.95% (0.04–20.53%)", "3"],
        ["Paroxetine", "5.42% (1.38–18.98%)", "11"],
        ["Fluvoxamine", "4.98% (3.79–6.52%)", "4"],
        ["Venlafaxine", "6.99% (1.05–34.61%)", "8"],
        ["Desvenlafaxine", "No pooled agent-specific estimate in this review", "—"],
        ["Duloxetine", "3.86% (0.07–71.04%)", "3"],
        ["Mirtazapine", "1.02% (0.25–4.02%)", "8"],
        ["Amitriptyline (TCA)", "2.05% (0.01–84.30%)", "3"],
    ],
})

slide("ssri-harms", "SSRIs are not free of kidney-related problems", """
- **Hyponatraemia:** first weeks; older age, thiazides, low body weight
- **QT prolongation:** citalopram and escitalopram are dose-related. In dialysis patients, potassium, calcium and magnesium shifts add risk
- **Serotonin toxicity:** watch tramadol, tapentadol, linezolid and ondansetron combinations
- **Falls and fractures:** on top of CKD–mineral bone disease
""")

# ---------------------------------------------------------------- 2. Lithium
question("q-li-decline", """
Peter, 56, has bipolar I disorder and has been well on lithium for 22 years. Level 0.7 mmol/L.

- eGFR has fallen from 78 to 46 over 10 years
- He passes about 4 L of urine a day
- Urine ACR is normal

What is the best next step?
""", [
    ("joint", "Continue lithium for now and arrange specialist review of renal function and polyuria"),
    ("reduce", "Reduce the lithium dose and repeat renal function in three months"),
    ("switch", "Arrange a gradual switch to another mood stabiliser because eGFR is below 60"),
    ("routine", "Continue the current regimen with routine monitoring because the lithium level is therapeutic"),
], "joint", """
This is classic **lithium-associated CKD** (chronic tubulointerstitial nephropathy) with **nephrogenic diabetes insipidus**. Decisions need to be shared between him, his psychiatrist and nephrology.

- **Reducing the dose alone** does not address the cause of the renal decline or polyuria; waiting three months delays assessment.
- **An eGFR below 60 alone** does not mandate switching. Weigh the renal trajectory against lithium’s benefit and the risks of relapse.
- **A therapeutic lithium level** does not exclude chronic renal adverse effects or justify routine monitoring alone.

The best window for the decision to continue or switch is early, while eGFR is still moderately preserved.
""")

slide("li-kidney", "Lithium and the kidney", """
- **Nephrogenic DI:** common (polyuria in up to about 1 in 3). Lithium enters collecting-duct cells through ENaC and blunts the response to ADH
- **Chronic tubulointerstitial nephropathy:** slow eGFR decline over years to decades; often bland urine and microcysts on imaging
- **Progression to kidney failure:** uncommon, but real after long exposure
- **Also:** hypercalcaemia (hyperparathyroidism) and hypothyroidism
- **Acute toxicity episodes** add to long-term kidney damage
""")

slide("li-monitor", "Monitoring and when to involve nephrology", """
Every 3–6 months: lithium level (12 h post-dose), U&E/eGFR, calcium and TSH. Check more often in older people and those with CKD.

Target for most adults is 0.6–0.8 mmol/L; use the lower end in older people.

**Involve nephrology when:**
- eGFR is <45, or falling steadily (for example, >5 mL/min/1.73m² a year)
- There is albuminuria or haematuria without another explanation
- Polyuria or nocturia is troublesome, or sodium is abnormal
- Calcium is raised
""")

slide("li-sick-days", "Lithium during acute illness", """
Vomiting, diarrhoea and poor fluid intake can precipitate lithium toxicity and AKI, especially with an ACE inhibitor, ARB, diuretic or NSAID.

- Withhold lithium during significant dehydrating illness and arrange same-day clinical review, lithium level and renal function/electrolytes
- Review other medicines that may need temporary withholding during dehydration
- Coarse tremor, ataxia, slurred speech, confusion, myoclonus or seizures require emergency assessment
- Restart lithium with a clinician-agreed plan once hydration and renal function are satisfactory; recheck levels as advised

""")


slide("li-interactions", "Drugs that move lithium levels", """
Recheck the lithium level about 5–7 days after starting, stopping or changing any of these.
""", table={
    "columns": ["Drug", "Effect on lithium", "Action"],
    "rowHeaders": True,
    "rows": [
        ["Thiazide diuretics", "↑ about 25–40%", "Avoid if possible; reduce dose and monitor if needed"],
        ["ACE inhibitors / ARBs", "↑ (variable)", "Often indicated in CKD: start, then recheck the level"],
        ["NSAIDs (incl. COX-2)", "↑", "Avoid; warn about over-the-counter use"],
        ["Loop diuretics", "↑ (smaller effect)", "Monitor"],
        ["SGLT2 inhibitors", "↓ (increased excretion)", "Monitor for loss of effect"],
        ["Amlodipine", "Minimal", "Reasonable antihypertensive choice"],
    ],
})

# ---------------------------------------------------------------- 3. Sedatives, gabapentinoids, antipsychotics


question("q-valproate-free", """
Ravi, 62, takes valproate for bipolar disorder. He has CKD stage 5 and albumin 25 g/L. He develops new drowsiness and tremor. His total valproate concentration is within the laboratory therapeutic range.

Which is the best interpretation?
""", [
    ("free", "A normal total level does not exclude toxicity: the free valproate fraction may be increased"),
    ("exclude", "The total level excludes valproate toxicity"),
    ("increase", "Low albumin means the dose should be increased"),
    ("renal", "Valproate is eliminated entirely unchanged by the kidneys"),
], "free", """
Renal failure and low albumin reduce valproate protein binding. The pharmacologically active free fraction may rise even when the total concentration appears therapeutic.

Assess urgently for medication toxicity and other causes of altered consciousness. Discuss a free valproate concentration where available; check ammonia when valproate-associated encephalopathy is suspected. Do not increase the dose simply to chase a total concentration.


Reference: [Valproate: renal disease and protein binding](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4b619f73-44e5-4a99-b425-a96cb2228c87).
""")

slide("gaba-dosing", "Gabapentinoid dosing by kidney function", """
Recommended total daily dose ranges. Always check the dose against CrCl.
""", table={
    "columns": ["CrCl (mL/min)", "Pregabalin", "Gabapentin"],
    "rowHeaders": True,
    "rows": [
        ["≥60", "150–600 mg", "900–3600 mg"],
        ["30–59", "75–300 mg", "400–1400 mg"],
        ["15–29", "25–150 mg", "200–700 mg"],
        ["<15", "25–75 mg", "100–300 mg"],
        ["Haemodialysis", "Plus 25–150 mg after each session", "Plus 125–350 mg after each session"],
    ],
})

question("q-antipsych", """
Daniel, 48, has schizophrenia and CKD stage 4 (CrCl 25 mL/min). At a routine GP appointment, you review a letter from his psychiatrist recommending a new oral antipsychotic.

Which of the following would most concern you about accumulation in renal impairment and prompt you to check the prescribed dose?
""", [
    ("pali", "Paliperidone"),
    ("olanz", "Olanzapine"),
    ("quet", "Quetiapine"),
    ("halo", "Haloperidol"),
], "pali", """
**Paliperidone** (the active metabolite of risperidone) is largely excreted unchanged by the kidney. At CrCl 10–50 the oral dose is reduced to 1.5 mg daily, and it is not recommended below CrCl 10. Long-acting injectable doses also need adjustment.

**Risperidone** needs a similar caution: reduce the dose by about 50%.

**Olanzapine, quetiapine and haloperidol** are hepatically metabolised and usually need no renal adjustment. Their problems in CKD are sedation, orthostasis, metabolic effects and QT prolongation.
""")

slide("sedatives", "Antipsychotics and sedatives in CKD", "", table={
    "columns": ["Drug", "Main concern in CKD", "Priority"],
    "rowHeaders": True,
    "rows": [
        ["Paliperidone", "Substantial renal elimination", "High"],
        ["Risperidone", "Active moiety accumulates", "High"],
        ["Quetiapine", "Sedation, orthostasis, QT", "Moderate"],
        ["Olanzapine", "Metabolic effects, sedation", "Moderate"],
        ["Diazepam", "Long half-life, active metabolites", "High: avoid"],
        ["Oxazepam / temazepam", "No active metabolites; still cause falls", "Prefer if a benzodiazepine is needed"],
        ["Zolpidem / zopiclone", "Falls, confusion", "Short courses only"],
    ],
})

question("q-insomnia", """
Anne, 74, has CKD stage 4 (CrCl 24 mL/min) and severe, short-term insomnia after a bereavement. Assessment has not identified depression, sleep apnoea, restless legs or uncontrolled pain/itch. She takes no opioids, drinks no alcohol and has no history of hypnotic dependence. Non-drug sleep strategies have started.

After discussing risks, she and her GP agree on a brief hypnotic trial. Which prescription is most appropriate?
""", [
    ("zopiclone-low", "Zopiclone 3.75 mg at night for up to 7 days, with a review and stop plan"),
    ("diazepam", "Diazepam 5 mg at night for up to 7 days, with a review and stop plan"),
    ("temazepam-long", "Temazepam 10 mg at night for 4 weeks before review"),
    ("zopiclone-full", "Zopiclone 7.5 mg at night for 4 weeks before review"),
], "zopiclone-low", """
**Zopiclone 3.75 mg for a brief trial** is the best of these options. The recommended starting dose in renal impairment is 3.75 mg, for short-term treatment (7–14 days). Review within a week, use the lowest effective dose and agree when to stop.

- **Diazepam** has a long half-life and active metabolites, increasing concern about prolonged sedation in an older person.
- **Temazepam** has no active metabolites and can be an alternative when a benzodiazepine is needed. The problem with this option is a four-week supply before review, not a claim that temazepam is always unsuitable in CKD.
- **Zopiclone 7.5 mg** is above the recommended starting dose for this patient; delaying review for four weeks is also inappropriate.

Zopiclone acts at the benzodiazepine receptor and still carries risks of falls, next-day impairment, dependence and rebound insomnia. Complex sleep behaviours are another important adverse effect. Do not combine it with a benzodiazepine, alcohol or other sedatives.


Continue non-drug treatment; persistent insomnia warrants reassessment and CBT-I.

Reference: [Zopiclone](https://www.safetyandquality.gov.au/medicine-finder/zopiclone-gh).
""")

slide("polypharmacy", "Stacking risk in dialysis patients", """
A typical haemodialysis medication list might include:
- Escitalopram, quetiapine and ondansetron, **plus**
- post-dialysis hypokalaemia and hypomagnesaemia

That adds up to QT stacking, and the risk is cumulative.

- Get a baseline ECG when combining QT-prolonging drugs
- Minimise anticholinergic burden (falls, delirium, constipation)
- Review sedatives at every opportunity
""")

# ---------------------------------------------------------------- 4. Transplant interactions
slide("tx-mechanism", "Calcineurin inhibitors: one mechanism, two dangers", """
Tacrolimus and ciclosporin are metabolised by **CYP3A4** and transported by **P-glycoprotein**, and both have a narrow therapeutic range.

Either direction is dangerous: too much causes toxicity, too little causes rejection.
""", table={
    "columns": ["", "Inhibitor added", "Inducer added"],
    "rowHeaders": True,
    "rows": [
        ["Tacrolimus metabolism", "↓", "↑"],
        ["Tacrolimus level", "↑", "↓"],
        ["Clinical result", "AKI, tremor, neurotoxicity, hyperkalaemia", "Under-immunosuppression, rejection, graft loss"],
        ["When the drug stops", "Level falls: rejection risk", "Level rises: toxicity risk"],
    ],
})



question("q-tx-cbz", """
Tom, 45, is 4 years post kidney transplant on tacrolimus, with stable creatinine around 120 µmol/L. A psychiatrist starts carbamazepine for bipolar disorder.

Three weeks later his creatinine is 165 µmol/L.

What is the most likely mechanism?
""", [
    ("induct", "CYP3A4 induction lowering tacrolimus, leading to acute rejection"),
    ("tox", "CYP3A4 inhibition raising tacrolimus, causing nephrotoxicity"),
    ("direct", "Direct carbamazepine nephrotoxicity"),
    ("siadh", "Carbamazepine-induced SIADH"),
], "induct", """
**Carbamazepine is a strong enzyme inducer.** Induction builds up over 2–3 weeks, tacrolimus levels fall, and rejection follows. This needs an urgent tacrolimus trough level and same-day contact with the transplant unit.

- **Inhibition** is the opposite mechanism; carbamazepine induces.
- Carbamazepine is not significantly **nephrotoxic**.
- **SIADH** causes hyponatraemia, not a creatinine rise.

Phenytoin, phenobarbital, rifampicin and St John's wort behave similarly. Oxcarbazepine is a weaker inducer but still needs specialist review and monitoring.
""")



slide("tx-table", "Psychotropic–immunosuppressant interactions", "", table={
    "columns": ["Drug", "Interaction", "Practical action"],
    "rowHeaders": True,
    "rows": [
        ["Fluoxetine", "Possible ↑ CNI", "Check interactions; monitor levels"],
        ["Sertraline", "Low potential", "Often reasonable; still review"],
        ["Escitalopram", "Limited CYP effect; QT", "ECG, electrolytes, other QT drugs"],
        ["Carbamazepine", "Strong induction: ↓↓ CNI", "Avoid where possible: rejection risk"],
        ["Oxcarbazepine", "Induction: ↓ CNI", "Specialist review and monitoring"],
        ["St John's wort", "Strong induction: ↓↓ CNI", "Avoid"],
        ["Quetiapine", "CYP3A4 substrate; QT, sedation", "Monitor, especially with azoles or diltiazem"],
    ],
})

slide("tx-actions", "What to do in practice", """
- **Contact the transplant team** when starting, stopping or changing an interacting psychotropic
- **Tacrolimus trough and creatinine** at about 5–7 days, then as advised
- **Remember the reversal:** when the interacting drug stops, levels swing back
- **Ciclosporin** is itself a CYP3A4 inhibitor and can raise levels of some psychotropics
- **Never adjust immunosuppression yourself.** Coordinate it
""")

# ---------------------------------------------------------------- 5. Psychiatric presentations caused by kidney medicines


slide("steroid-risk", "Steroid psychiatric effects are dose-related", """
Classic incidence of psychiatric reactions by daily prednisolone-equivalent dose (Boston Collaborative Drug Surveillance Program):
""", table={
    "columns": ["Daily dose", "Incidence"],
    "rows": [
        ["≤40 mg", "about 1%"],
        ["41–80 mg", "about 5%"],
        [">80 mg", "about 18%"],
    ],
    "caption": "Psychiatric reactions to corticosteroids",
})


# ---------------------------------------------------------------- 6. Final case and checklist
question("q-memantine", """
George, 80, has Alzheimer disease and CKD stage 4. His estimated CrCl is 22 mL/min. A letter proposes increasing immediate-release memantine from 5 mg twice daily to 10 mg twice daily.

What should the GP do?
""", [
    ("check", "Query the increase: severe renal impairment requires a lower target dose"),
    ("usual", "Increase as proposed because cognitive medicines do not need renal adjustment"),
    ("stop", "Stop all cognitive treatment because CKD stage 4 is an absolute contraindication"),
    ("double", "Double the dose because renal impairment reduces absorption"),
], "check", """
Memantine exposure increases in renal impairment. For immediate-release tablets, the recommended target dose is 5 mg twice daily at CrCl 5–29 mL/min. Do not routinely increase this patient to 10 mg twice daily.

Confirm the recommendation for the prescribed formulation. Monitor dizziness, confusion and falls; new cognitive deterioration also needs assessment for delirium.


Reference: [Memantine, immediate release](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=30b4d5c4-0a31-c385-e063-6394a90adbce).
""")

question("q-acamprosate", """
Leanne, 54, has alcohol dependence and CKD stage 4, with estimated CrCl 24 mL/min. After completing withdrawal treatment she asks about acamprosate to help maintain abstinence.

What is the best next step?
""", [
    ("avoid", "Avoid acamprosate at this kidney function and discuss an alternative relapse-prevention plan"),
    ("full", "Start the usual full dose because acamprosate is not hepatically metabolised"),
    ("half", "Start half the usual dose without further review"),
    ("withdrawal", "Use acamprosate to treat acute alcohol withdrawal"),
], "avoid", """
Acamprosate is renally eliminated. It is contraindicated at CrCl ≤30 mL/min. A reduced dose for moderate impairment does not make it suitable at CrCl 24.

Discuss alternative pharmacological and psychosocial treatment with the addiction service, considering liver function, opioid use and other contraindications. Acamprosate maintains abstinence; it does not treat acute withdrawal.


Reference: [Acamprosate: renal impairment](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5ebfa8c9-acba-b77e-e063-6294a90ab712).
""")

slide("cases-intro", "Putting it together: a dialysis case", """
Choosing treatment when low mood, poor sleep, appetite loss and itch overlap.
""")

question("q-case-hd", """
Mohammed, 67, is on haemodialysis. He has low mood, poor sleep, poor appetite and itch.

Which is the best initial medication option?
""", [
    ("mirt", "Mirtazapine 7.5 mg at night"),
    ("ami", "Amitriptyline 25 mg at night"),
    ("diaz", "Diazepam 5 mg at night"),
    ("desv", "Desvenlafaxine 100 mg daily"),
], "mirt", """
**Low-dose mirtazapine** helps sleep and appetite, may ease uraemic pruritus, and is a reasonable antidepressant on dialysis. Its clearance is reduced, so start at 7.5 mg and titrate slowly while watching for sedation and falls.

- **Amitriptyline:** anticholinergic, orthostatic and QT effects.
- **Diazepam:** active metabolites accumulate.
- **Desvenlafaxine:** at most 50 mg every second day on dialysis.

Also check dialysis adequacy, phosphate, PTH and iron. Itch has many treatable contributors.
""")


slide("checklist", "GP prescribing checklist", """
1. Know the **current eGFR/CrCl** and whether the patient is on dialysis
2. Is the drug **renally cleared**, does it **accumulate**, or is it **nephrotoxic**?
3. **Start low, go slow.** Review sedation, falls and cognition
4. Check **Na, K, Mg** and an **ECG** when combining QT-prolonging drugs
5. **Lithium:** level, eGFR, Ca and TSH every 3–6 months; give sick-day rules in writing
6. **Transplant:** check every new, stopped or changed drug, including herbal ones, for CYP3A4 effects. Tell the transplant team
7. New psychiatric symptoms on steroids or a calcineurin inhibitor: **exclude organic causes first**
""")

slide("take-home", "Take-home messages", """
- **Sertraline** (or low-dose **mirtazapine**) is a sensible start in advanced CKD; expect modest benefit
- **Lithium:** monitor, write down sick-day rules, and involve nephrology early
- **Gabapentinoids** cause encephalopathy and myoclonus in CKD: dose to CrCl
- **Interactions:** carbamazepine and St John's wort can lower tacrolimus levels; fluoxetine may increase levels. Coordinate changes with the transplant team
- **Confusion, seizures, headache or visual change** on tacrolimus is an emergency
""")

slide("refs", "Key references", """
- [Gheysens T et al. Antidepressant-induced hyponatremia: meta-analysis. European Psychiatry 2024;67:e20](https://doi.org/10.1192/j.eurpsy.2024.11)
- Hedayati SS et al. Effect of sertraline on depressive symptoms in CKD (CAST). JAMA 2017;318:1876–90
- Mehrotra R et al. Comparative efficacy of therapies for depression in haemodialysis (ASCEND). Ann Intern Med 2019;170:369–79
- Nagler EV et al. Antidepressants for depression in stage 3–5 CKD: a systematic review. Nephrol Dial Transplant 2012;27:3736–45
- Cohen LM et al. Update on psychotropic medication use in renal disease. Psychosomatics 2004;45:34–48
- Malhi GS et al. RANZCP clinical practice guidelines for mood disorders. Aust N Z J Psychiatry 2021;55:7–117
- Davis J et al. Lithium and nephrotoxicity: approaches to clinical management. BMC Nephrol 2018;19:305
- Decker BS et al. Extracorporeal treatment for lithium poisoning (EXTRIP). Clin J Am Soc Nephrol 2015;10:875–87
- Bechstein WO. Neurotoxicity of calcineurin inhibitors. Transpl Int 2000;13:313–26
- Boston Collaborative Drug Surveillance Program. Acute adverse reactions to prednisone. Clin Pharmacol Ther 1972;13:694–8
- Australian Medicines Handbook; TGA product information
- [BC Transplant: Medication guidelines for solid organ transplants](https://www.transplant.bc.ca/Documents/Statistics/Clinical%20Guidelines%20for%20Transplant%20Medications.pdf)
- [NIDDK: Drug dosing in adults with CKD](https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/ckd-drug-dosing-providers)
""")


lesson = {
    "schemaVersion": 1,
    "id": "tdc-2026-psych-pharm-kidney",
    "title": "Psychiatric pharmacotherapy in kidney disease and transplantation",
    "steps": steps,
}


# ---------------------------------------------------------------- Validation
def validate(lesson):
    errors = []
    schema_path = HERE / "lesson.schema.json"
    if schema_path.exists():
        import jsonschema
        schema = json.loads(schema_path.read_text())
        for e in jsonschema.Draft7Validator(schema).iter_errors(lesson):
            errors.append(f"schema: {list(e.absolute_path)}: {e.message[:200]}")
    else:
        print("warning: lesson.schema.json not found; skipping schema check")
    ids = [s["id"] for s in lesson["steps"]]
    dups = {i for i in ids if ids.count(i) > 1}
    if dups:
        errors.append(f"duplicate step ids: {dups}")
    for s in lesson["steps"]:
        if s["type"] == "question":
            oids = [o["id"] for o in s["options"]]
            if len(set(oids)) != len(oids):
                errors.append(f"{s['id']}: duplicate option ids")
            if s["correctOptionId"] not in oids:
                errors.append(f"{s['id']}: correctOptionId not in options")
        t = s.get("table")
        if t:
            n = len(t["columns"]) if "columns" in t else len(t["rows"][0])
            for r in t["rows"]:
                if len(r) != n:
                    errors.append(f"{s['id']}: table row length {len(r)} != {n}")
    return errors


out = json.dumps(lesson, ensure_ascii=False, indent=2)
errs = validate(lesson)
size = len(out.encode())
if size >= 256 * 1024:
    errs.append(f"file too large: {size} bytes")
if errs:
    print("\n".join(errs))
    sys.exit(1)
(HERE / "lesson.json").write_text(out + "\n")
nq = sum(s["type"] == "question" for s in steps)
print(f"lesson.json written: {len(steps)} steps ({nq} questions), {size} bytes")
