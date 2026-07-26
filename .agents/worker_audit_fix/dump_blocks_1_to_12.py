import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

blocks = []
in_block = False
start = 0
b_lines = []

for i, line in enumerate(lines):
    if line.strip().startswith("```mermaid"):
        in_block = True
        start = i + 1
        b_lines = []
    elif in_block and line.strip() == "```":
        in_block = False
        end = i + 1
        blocks.append((start, end, b_lines))
    elif in_block:
        b_lines.append(line)

print(f"Total Mermaid blocks found: {len(blocks)}")
for idx, (s, e, b_lines) in enumerate(blocks, 1):
    print(f"\n============================================================")
    print(f"BLOCK #{idx} (Lines {s} to {e})")
    print(f"============================================================")
    for l in b_lines:
        print(l.rstrip())
    print("--- Following text (next 12 lines) ---")
    for fl in lines[e:min(e+12, len(lines))]:
        print(fl.rstrip())
