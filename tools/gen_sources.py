"""Regenerate docs/sources.md from the links in the evidence tables.

Usage: python3 tools/gen_sources.py .
"""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1])
groups = [
    ("Shared landscape", "docs/landscape.md"),
    ("Port and route readiness", "docs/readiness/evidence.md"),
    ("Independent reactor monitoring", "docs/monitoring/evidence.md"),
    ("Insurance for nuclear ships", "docs/insurance/evidence.md"),
    ("Shielding and layout optimizer (backup)", "docs/shielding/research.md"),
]
link = re.compile(r'\[([^\]]+)\]\((https?://[^()\s]+(?:\([^)]*\))?[^()\s]*)\)')
out = ["# Sources", "", "[Back to README](../README.md) · [Landscape](landscape.md) · [Portfolio](portfolio.md)", "",
       "Checked October 7, 2026. Every evidence row links its own source; this page lists them by area, without duplicates. Generated from the evidence tables, so fix a link there, not here.", ""]
for title, rel in groups:
    text = (root / rel).read_text()
    seen = {}
    for name, url in link.findall(text):
        if url not in seen:
            seen[url] = name
    out.append(f"## {title}")
    out.append("")
    out.append(f"From [{rel.split('docs/')[1]}]({rel.split('docs/')[1]}).")
    out.append("")
    for url, name in seen.items():
        out.append(f"- [{name}]({url})")
    out.append("")
(root / "docs/sources.md").write_text("\n".join(out))
print(sum(1 for l in out if l.startswith("- [")), "links written")
