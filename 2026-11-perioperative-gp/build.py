#!/usr/bin/env python3
"""Build and validate the 15-minute GP lesson: python3 build.py.

Clinical sources and delivery notes: presenter-notes.txt and sources.txt.
Fimbria format: https://fimbria.lattice-1.com/docs/lesson-format.md
"""
import json
from pathlib import Path
import re
import sys

import jsonschema

HERE = Path(__file__).resolve().parent
steps = []


def slide(id, title, body):
    steps.append(dict(id=id, type="slide", title=title, body=body.strip()))


def question(id, case, ask, options, correct, explanation, clues):
    """Underline evidence on a reading slide; keep the voting prompt plain."""
    body = case
    for clue in clues:
        if body.count(clue) != 1 or "\n" in clue:
            raise ValueError(f"Ambiguous or multiline clue: {clue!r}")
        body = body.replace(clue, f"[underline]{clue}[/underline]", 1)
    number = 1 + sum(s["type"] == "question" for s in steps)
    slide(id + "-clues", f"Case {number}: read the clues", body)
    steps.append(dict(
        id=id, type="question", prompt=case + "\n\n" + ask,
        options=[dict(id=k, text=v) for k, v in options],
        correctOptionId=correct, explanation=explanation.strip(),
    ))


slide("intro", "Perioperative medication optimisation: five GP decisions", """
A 15-minute guide to chronic disease medicines before elective surgery.
- GLP-1 medicines, anticoagulants and rheumatoid arthritis biologics
- SGLT2 inhibitors and ACE inhibitors/ARBs
- Leave with a written **last dose, restart and review plan**
Australian practice focus • Guidance checked 17 November 2026
Agree the plan with the procedural and anaesthetic teams.
""")

question(
    "q-glp1",
    "Helen, 58, takes weekly semaglutide for type 2 diabetes. She has been on a stable dose for six months and has no gastrointestinal symptoms. She is booked for elective laparoscopic surgery under general anaesthesia in two weeks.",
    "Under current Australian guidance, which plan is most appropriate?",
    [
        ("stop-week", "Omit semaglutide for one week, then use ordinary fasting instructions alone"),
        ("continue-diet", "Continue semaglutide; arrange the recommended clear-fluid diet and anaesthetic fasting plan"),
        ("ordinary-fast", "Continue semaglutide; ordinary fasting alone is enough because she has no symptoms"),
        ("stop-month", "Stop semaglutide for four weeks and restart automatically on the day after surgery"),
    ],
    "continue-diet",
    """
Australian guidance recommends [underline]continuing GLP-1 and dual GLP-1/GIP medicines[/underline], with a 24-hour clear-fluid diet before the procedure, followed by the anaesthetic fasting instructions. Lack of symptoms does not exclude retained gastric contents.
- ANZCA clarifies: water only in the final six hours; nothing by mouth in the final two hours. Obtain the hospital's exact timings.
- A routine one-week omission does not reliably remove the gastric-emptying risk; four weeks is not the routine recommendation.
- If the diet was not followed, or symptoms or recent dose escalation raise concern, contact anaesthesia for assessment and a proceeding/postponement plan.
GP action: reconcile other diabetes medicines and glucose monitoring during the diet. (Ref 1)
""",
    ("weekly semaglutide", "general anaesthesia"),
)

question(
    "q-apixaban",
    "David, 72, takes apixaban 5 mg twice daily for atrial fibrillation. His CrCl is 70 mL/min, with no recent stroke or venous thromboembolism. He is having a high-bleeding-risk abdominal operation on Friday morning. General anaesthesia is planned, without spinal or epidural anaesthesia.",
    "Which apixaban plan should the GP confirm with the surgical team?",
    [
        ("morning-only", "Omit only Friday morning's dose and resume the full dose on Friday evening"),
        ("bridge", "Omit Wednesday to Friday and use therapeutic-dose enoxaparin as a bridge"),
        ("short-hold", "Take the last dose Wednesday evening; omit Thursday and Friday; resume the full dose on Saturday"),
        ("timed-hold", "Take the last dose Tuesday evening; omit Wednesday to Friday; plan resumption after haemostasis"),
    ],
    "timed-hold",
    """
For this standard-dose apixaban case, [underline]omit the two days before and the day of surgery[/underline]: last dose Tuesday evening for Friday surgery. Therapeutic-dose heparin bridging is not indicated.
- Resume therapeutic apixaban usually 48–72 hours after high-bleeding-risk surgery, once haemostasis and oral intake permit; the surgical team confirms timing.
- Postoperative prophylactic anticoagulation, when safe, is a separate decision from therapeutic bridging.
- A morning-only omission is too short. The Wednesday-last-dose option uses the shorter interruption for lower bleeding risk and restarts too early for this case.
This schedule is not transferable to every anticoagulant: renal impairment, dabigatran, spinal/epidural procedures and very high thrombotic risk need a specific plan. (Ref 2)
""",
    ("apixaban 5 mg twice daily", "high-bleeding-risk"),
)

question(
    "q-biologic",
    "Ruth, 61, has rheumatoid arthritis controlled with adalimumab every two weeks and weekly methotrexate. Renal function and blood counts are normal. She is awaiting total knee replacement. After discussing infection and flare risks, her rheumatologist and surgeon have agreed to interrupt adalimumab for one dosing interval.",
    "Which plan best implements that decision?",
    [
        ("interval", "Continue methotrexate; miss the next adalimumab dose and arrange surgery in week 3 after the last injection"),
        ("stop-all", "Stop both medicines for six weeks before surgery and six weeks afterwards"),
        ("day-only", "Continue methotrexate; omit adalimumab only if an injection falls on the day of surgery"),
        ("auto-restart", "Miss the next adalimumab dose, then restart it on day 3 regardless of wound healing"),
    ],
    "interval",
    """
When the team elects to withhold fortnightly adalimumab, [underline]miss one dose; operate in week 3 after the last injection[/underline]. Methotrexate is usually continued in this uncomplicated case.
- Restart adalimumab only when the wound is healing, sutures/staples are out and there is no infection, often around 14 days; obtain team approval.
- Stopping everything for weeks increases flare risk; omitting only the surgery-day dose does not implement the agreed interval.
Guidance differs: Australian recommendations do not routinely stop all biologics, but consider interruption for higher infection risk or consequences. ACR/AAHKS favours withholding biologics for hip/knee replacement. The case explicitly uses an agreed interruption plan. (Refs 3–4)
""",
    ("adalimumab every two weeks", "interrupt adalimumab for one dosing interval"),
)

question(
    "q-sglt2",
    "Michael, 66, takes morning empagliflozin for type 2 diabetes and heart failure. Elective major abdominal surgery is booked for Friday, with an inpatient stay. At Monday's GP visit, he asks whether he should take empagliflozin until Thursday because his glucose readings are normal.",
    "Which is the best plan for this Australian inpatient-surgery scenario?",
    [
        ("glucose", "Continue until Thursday because normal glucose excludes ketoacidosis risk"),
        ("day-only", "Omit Friday's dose only and restart on Saturday even if still fasting"),
        ("planned-hold", "Last dose Tuesday morning; omit Wednesday, Thursday and Friday; agree monitoring and restart criteria"),
        ("glucose-restart", "Omit Wednesday to Friday, then restart as soon as glucose rises even if still fasting"),
    ],
    "planned-hold",
    """
ADS–ANZCA guidance for surgery with an inpatient stay is to [underline]omit SGLT2 inhibitors for two days before and the day of surgery[/underline]. In this morning-dose example, Tuesday is the last dose before Friday surgery.
- Fasting and surgical stress can cause ketoacidosis despite a near-normal glucose. Nausea, abdominal pain, rapid breathing or unexplained illness require urgent assessment with blood ketones and acid–base testing.
- Restart only when eating and drinking normally, clinically stable and free of ketosis, with the treating team's agreement.
- Heart failure benefit does not remove this perioperative risk; a rising glucose alone is not a safe restart criterion.
Confirm local instructions: some protocols use longer holds, particularly for ertugliflozin. (Ref 5)
""",
    ("morning empagliflozin", "major abdominal surgery"),
)

question(
    "q-ace-arb",
    "Anne, 69, takes perindopril solely for hypertension. BP is 126/74 mmHg; she has no heart failure. She is preparing for elective major vascular surgery. Her pre-anaesthetic medication plan has not yet been completed.",
    "Which recommendation is most appropriate to discuss with anaesthesia?",
    [
        ("continue-all", "Continue perindopril without seeking anaesthetic advice because her blood pressure is well controlled"),
        ("individualise", "Consider omitting perindopril 24 hours beforehand to limit hypotension; document when to restart"),
        ("stop-all", "Withhold perindopril and every other antihypertensive for 48 hours before surgery"),
        ("hf-same", "Use the same mandatory ACE inhibitor hold for all patients with reduced-ejection-fraction heart failure"),
    ],
    "individualise",
    """
For controlled hypertension before elevated-risk noncardiac surgery, [underline]omission of an ACE inhibitor or ARB 24 hours beforehand may reduce intraoperative hypotension[/underline]. It is an option to agree with anaesthesia, not a universal rule.
- If prescribed for heart failure with reduced ejection fraction, continuation may be reasonable; indication changes the balance.
- Trials have not shown that routine withholding improves major postoperative outcomes. Stopping every antihypertensive is inappropriate; a controlled BP does not remove the need for an agreed plan.
- If withheld, document reassessment and restart once blood pressure, volume status, renal function and potassium allow. Prevent accidental long-term omission.
GP action: record why each medicine is prescribed before deciding whether to interrupt it. (Ref 6)
""",
    ("solely for hypertension", "no heart failure"),
)

slide("checklist", "The GP handover: make every instruction actionable", """
1. Reconcile medicines, indication, renal function and procedure/anaesthetic risk.
2. Write the **last dose date and time**; include fasting and glucose instructions.
3. Name the clinician responsible for **restart and review**.
4. State restart conditions: bleeding, oral intake, wound, BP and kidney function.
5. Give the patient and procedural team the same written plan.
[underline]Every temporary hold needs a restart plan.[/underline]
""")

slide("references", "Guidance behind the five decisions", """
1. ANZCA: GLP-1 peri-procedural recommendations and current fasting FAQs.
2. Tran et al. DOAC guidelines. Internal Medicine Journal 2025. doi:10.1111/imj.70103
3. Buchbinder et al. Australian perioperative DMARD recommendations. 2023. doi:10.1111/imj.16073
4. ACR/AAHKS hip/knee arthroplasty guideline. 2022. doi:10.1002/art.42140
5. ADS–ANZCA perioperative diabetes guideline. 2022, section 6.1.2 and Appendix L.
6. AHA/ACC perioperative cardiovascular guideline, reaffirmed 2026, section 7.2.
Full source links and delivery notes accompany this lesson.
""")

lesson = dict(
    schemaVersion=1, id="gp-perioperative-medication-2026",
    title="Perioperative medication optimisation: five GP decisions", steps=steps,
)


def validate():
    schema = json.loads((HERE / "lesson.schema.json").read_text())
    jsonschema.Draft7Validator(schema).validate(lesson)
    ids = [s["id"] for s in steps]
    assert len(ids) == len(set(ids)), "Duplicate step IDs"
    assert sum(s["type"] == "question" for s in steps) == 5
    for i, s in enumerate(steps):
        if s["type"] == "question":
            options = [o["id"] for o in s["options"]]
            assert len(options) == len(set(options))
            assert s["correctOptionId"] in options
            assert steps[i - 1]["id"] == s["id"] + "-clues"
            for text in [s["prompt"], *(o["text"] for o in s["options"])]:
                assert not re.search(r"\[/?(?:underline|marker|fade)\]|\*\*|==", text)
        for field in ("body", "explanation"):
            text = s.get(field, "")
            pairs = re.findall(r"\[underline\](\S(?:[^\n]*?\S)?)\[/underline\]", text)
            assert text.count("[underline]") == text.count("[/underline]") == len(pairs)
            assert len(pairs) <= 2, "Keep animation sparse"
        for field in ("title", "prompt"):
            assert "[underline]" not in s.get(field, "")


if __name__ == "__main__":
    try:
        validate()
        output = json.dumps(lesson, ensure_ascii=False, indent=2) + "\n"
        assert len(output.encode()) < 256 * 1024
        (HERE / "lesson.json").write_text(output)
    except (AssertionError, jsonschema.ValidationError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"Validated lesson.json: {len(steps)} steps, 5 questions, {len(output.encode())} bytes")
