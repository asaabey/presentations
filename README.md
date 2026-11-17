# Presentations

Clinical teaching presentations and Fimbria lessons for general practice.

| Presentation | Lesson | Readable copy |
| --- | --- | --- |
| Psychiatric pharmacotherapy in kidney disease and transplantation | [Fimbria JSON](2026-11-tdc/lesson.json) | [Text](2026-11-tdc/lesson.txt) |
| Perioperative medication optimisation: five GP decisions | [Fimbria JSON](2026-11-perioperative-gp/lesson.json) | [Text](2026-11-perioperative-gp/lesson.txt) |

## Use with Fimbria

Upload a `lesson.json` file, or import its public GitHub URL into Fimbria.
Re-import after changes to update an existing saved lesson.

- [Kidney disease and psychiatric medicines](https://github.com/asaabey/presentations/blob/main/2026-11-tdc/lesson.json)
- [Perioperative medication optimisation](https://github.com/asaabey/presentations/blob/main/2026-11-perioperative-gp/lesson.json)

Each presentation folder includes its build script and supporting materials.
To rebuild a lesson, install Python 3 and `jsonschema`, then run from its folder:

```bash
python3 build.py
python3 export_text.py
```

The perioperative lesson includes a 15-minute delivery plan in
[presenter-notes.txt](2026-11-perioperative-gp/presenter-notes.txt) and a
[source register](2026-11-perioperative-gp/sources.txt).
