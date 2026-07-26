import re
import sys

target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")

mermaid_blocks = []
in_mermaid = False
start_line = 0
current_block = []

for idx, line in enumerate(lines, 1):
    if line.strip().startswith("```mermaid"):
        if in_mermaid:
            print(f"ERROR: Nested or unclosed ```mermaid block before line {idx}")
        in_mermaid = True
        start_line = idx
        current_block = []
    elif line.strip() == "```" and in_mermaid:
        in_mermaid = False
        end_line = idx
        mermaid_blocks.append((start_line, end_line, "".join(current_block)))
        current_block = []
    elif in_mermaid:
        current_block.append(line)

if in_mermaid:
    print(f"ERROR: Unclosed ```mermaid block starting at line {start_line}")

print(f"Found {len(mermaid_blocks)} Mermaid blocks.")

for i, (s, e, content) in enumerate(mermaid_blocks, 1):
    print(f"\n--- Block {i} (Lines {s}-{e}) ---")
    header = content.strip().splitlines()[0] if content.strip() else "EMPTY"
    print(f"Header/Type: {header}")
    print(f"Content lines count: {len(content.splitlines())}")
