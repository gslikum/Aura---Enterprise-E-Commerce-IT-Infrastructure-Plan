import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

mermaid_matches = list(re.finditer(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL))

for idx, match in enumerate(mermaid_matches, 1):
    block_str = match.group(1)
    print(f"=== MERMAID BLOCK {idx} ===")
    lines = block_str.splitlines()
    for l_num, line in enumerate(lines, 1):
        print(f"  Line {l_num:02d}: {line}")
    print()

