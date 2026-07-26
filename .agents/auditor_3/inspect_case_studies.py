import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

case_study_start = re.search(r"#+\s*Case\s+Study\s+Questions", content, re.IGNORECASE)
if not case_study_start:
    # Look for case studies throughout document
    print("Searching for Case Studies throughout document...")
    matches = re.findall(r"(#+\s*.*[Cc]ase.*)", content)
    for m in matches:
        print("  Found heading:", m)
else:
    print("Found Case Study section header at index:", case_study_start.start())
    cs_text = content[case_study_start.start():]
    headings = re.findall(r"(#+\s*.*)", cs_text)
    for h in headings[:30]:
        print("  ", h)

print("\n--- Detailed Case Studies Search across entire file ---")
cs_sections = re.findall(r"(#+\s*.*Case.*?\n(?:(?!^#).*\n)+)", content, re.IGNORECASE)
print(f"Total Case Study sections matched: {len(cs_sections)}")
for idx, cs in enumerate(cs_sections, 1):
    first_lines = "\n".join([line for line in cs.splitlines() if line.strip()][:5])
    print(f"\n--- Case Study Block {idx} ---")
    print(first_lines)

