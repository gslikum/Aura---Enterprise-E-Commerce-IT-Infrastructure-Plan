import re

target_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(target_path, "r", encoding="utf-8") as f:
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
        start_idx = idx # 0-based
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
    print(f"MERMAID BLOCK #{i} (Lines {s+1} to {e+1})")
    print(f"==========================================")
    for l in blines:
        print(l)
    print("--- Following 10 lines after block ---")
    for fl in lines[e+1:min(e+11, len(lines))]:
        print(fl)
