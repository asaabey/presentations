#!/usr/bin/env python3
"""Render lesson.json as plain text for terminal review: python3 export_text.py"""
import json, pathlib, re, textwrap

HERE = pathlib.Path(__file__).parent
lesson = json.loads((HERE / "lesson.json").read_text())
W = 80
out = []

def clean(s):
    s = re.sub(r"\[(marker|underline|fade)\](\S(?:[^\n]*?\S)?)\[/\1\]", lambda m: m.group(2), s)
    return re.sub(r"\*\*(.+?)\*\*|==(.+?)==", lambda m: m.group(1) or m.group(2), s)

def para(s, indent=""):
    for line in clean(s).splitlines():
        if not line.strip():
            out.append("")
            continue
        m = re.match(r"^(\s*(?:[-*•]|\d+[.)])\s+)", line)
        sub = indent + " " * len(m.group(1)) if m else indent
        out.append(textwrap.fill(line, W, initial_indent=indent, subsequent_indent=sub))

def table(t, indent="    "):
    rows = ([t["columns"]] if "columns" in t else []) + [[str(c) for c in r] for r in t["rows"]]
    if t.get("caption"):
        out.append(indent + t["caption"])
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    for n, r in enumerate(rows):
        out.append(indent + " | ".join(c.ljust(w) for c, w in zip(r, widths)).rstrip())
        if n == 0 and "columns" in t:
            out.append(indent + "-+-".join("-" * w for w in widths))

out += ["=" * W, lesson["title"], "=" * W, ""]
q = 0
for i, s in enumerate(lesson["steps"], 1):
    if s["type"] == "question":
        q += 1
        out.append(f"--- [{i}] Q{q}  ({s['id']}) " + "-" * max(0, W - 16 - len(s['id'])))
        para(s["prompt"])
        if s.get("table"):
            out.append(""); table(s["table"])
        out.append("")
        for n, o in enumerate(s["options"]):
            mark = "*" if o["id"] == s["correctOptionId"] else " "
            out.append(textwrap.fill(f"{mark} {chr(65+n)}. {o['text']}", W, subsequent_indent="     "))
        ans = next(chr(65+n) for n, o in enumerate(s["options"]) if o["id"] == s["correctOptionId"])
        out += ["", f"  ANSWER: {ans}", "  EXPLANATION:"]
        para(s["explanation"], indent="    ")
    elif s["type"] == "slide":
        out.append(f"--- [{i}] SLIDE: {s['title']}  ({s['id']})")
        if s["body"]:
            para(s["body"])
        if s.get("table"):
            out.append(""); table(s["table"])
    else:
        out.append(f"--- [{i}] VIDEO: {s['title']}  {s['src']}")
    out.append("")

(HERE / "lesson.txt").write_text("\n".join(out) + "\n")
print(f"lesson.txt written ({len(out)} lines)")
