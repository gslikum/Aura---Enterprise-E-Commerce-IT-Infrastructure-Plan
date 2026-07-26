target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

blocks = []
in_b = False
s_line = 0
cur = []

for idx, line in enumerate(lines, 1):
    if line.strip().startswith("```mermaid"):
        in_b = True
        s_line = idx
        cur = []
    elif line.strip() == "```" and in_b:
        in_b = False
        blocks.append((s_line, idx, cur))
        cur = []
    elif in_b:
        cur.append((idx, line))

print(f"Total Mermaid blocks found: {len(blocks)}\n")

for i, (s, e, c_lines) in enumerate(blocks, 1):
    print(f"==================================================")
    print(f"BLOCK {i} (File Lines {s} to {e})")
    print(f"==================================================")
    for lno, text in c_lines:
        print(f"{lno:4d}: {text}", end="")
    print("\n")
