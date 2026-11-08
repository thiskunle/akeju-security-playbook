# Copyright (c) 2026 Adekunle Akeju. All rights reserved except as licensed.
# Small Business Security Playbook by Adekunle Akeju, created by Adekunle Akeju. SPDX-License-Identifier: CC-BY-SA-4.0
"""Checks that links resolve, each template credits its author, and checklists are well formed."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parents[1]
errors = []

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for target in re.findall(r"\]\((?!https?:|mailto:)([^)#]+)\)", readme):
    if not (ROOT / target).exists():
        errors.append(f"README links to missing file: {target}")

templates = sorted((ROOT / "templates").glob("*.md"))
for path in templates:
    text = path.read_text(encoding="utf-8")
    if "Adekunle Akeju" not in "\n".join(text.splitlines()[:4]):
        errors.append(f"{path.name}: author credit missing from the top")
    if not text.startswith("# "):
        errors.append(f"{path.name}: needs a title")
    if path.name not in readme:
        errors.append(f"{path.name}: not listed in the README")
    for line in text.splitlines():
        if re.match(r"\s*- \[.?\]", line) and not re.match(r"\s*- \[ \] \S", line):
            errors.append(f"{path.name}: malformed checkbox: {line}")

if not templates:
    errors.append("No templates found.")
print("\n".join(errors) or f"OK: {len(templates)} templates checked.")
sys.exit(1 if errors else 0)
