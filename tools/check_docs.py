"""Check markdown docs: relative links resolve, #anchors exist, no em or en dashes.

Usage: python3 tools/check_docs.py .
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1]).resolve()
files = [p for p in root.rglob("*.md") if ".git" not in p.parts]
link = re.compile(r'(?<!!)\[[^\]]*\]\(([^()\s]+(?:\([^)]*\))?[^()\s]*)\)')

def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')

def anchors(path):
    out, in_code = set(), False
    for line in path.read_text().splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r'#{1,6} ', line):
            out.add(slug(line.lstrip('#')))
    return out

errors = 0
for f in files:
    text = f.read_text()
    for n, line in enumerate(text.splitlines(), 1):
        if "—" in line or "–" in line:
            print(f"{f.relative_to(root)}:{n}: em or en dash"); errors += 1
    for target in link.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, frag = target.partition("#")
        dest = (f.parent / path).resolve() if path else f
        if not dest.exists():
            print(f"{f.relative_to(root)}: missing file {target}"); errors += 1
            continue
        if frag and dest.is_file() and frag not in anchors(dest):
            print(f"{f.relative_to(root)}: missing anchor {target}"); errors += 1
print(f"{len(files)} files checked, {errors} problems")
sys.exit(1 if errors else 0)
