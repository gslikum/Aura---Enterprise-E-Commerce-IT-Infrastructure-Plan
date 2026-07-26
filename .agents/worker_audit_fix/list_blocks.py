import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

blocks = []
start = -1
for i, line in enumerate(lines, 1):
    if line.strip().startswith("```mermaid"):
        start = i
    elif start != -1 and line.strip().startswith("```"):
        blocks.append((start, i))
        start = -1

print(f"Total blocks: {len(blocks)}")
for idx, (s, e) in enumerate(blocks, 1):
    print(f"Block #{idx}: Lines {s} to {e}")
    # print diagram code
    diagram_code = lines[s:e-1]
    for dl in diagram_code:
        print(f"  {dl.rstrip()}")
    # print following 6 lines
    print("  --- Following text ---")
    for fl in lines[e:min(e+6, len(lines))]:
        print(f"  + {fl.rstrip()}")
    print("="*60)
