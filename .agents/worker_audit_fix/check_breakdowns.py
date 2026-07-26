import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

# Find all mermaid blocks
mermaid_blocks = []
in_block = False
start_idx = 0
block_lines = []

for idx, line in enumerate(lines):
    if line.strip() == "```mermaid":
        in_block = True
        start_idx = idx
        block_lines = []
    elif in_block and line.strip() == "```":
        in_block = False
        end_idx = idx
        mermaid_blocks.append((start_idx, end_idx, block_lines))
    elif in_block:
        block_lines.append(line)

print(f"Total Mermaid blocks: {len(mermaid_blocks)}")

for i, (s, e, blines) in enumerate(mermaid_blocks, 1):
    print(f"\n==========================================")
    print(f"DIAGRAM #{i} (Line {s+1} to {e+1})")
    print(f"==========================================")
    # Print next 20 lines after diagram
    after_lines = lines[e+1:e+25]
    for al in after_lines:
        if al.strip().startswith("## ") and not al.strip().startswith("### Explanatory Breakdown"):
            break
        print(al)
