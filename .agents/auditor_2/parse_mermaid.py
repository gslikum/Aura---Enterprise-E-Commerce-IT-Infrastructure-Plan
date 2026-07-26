import re

file_path = '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

mermaid_blocks = []
start = None
code_lines = []

for idx, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('```mermaid'):
        start = idx
        code_lines = []
    elif (s == '```' or s.startswith('```')) and start is not None:
        end = idx
        # Find next non-empty line
        next_line = ''
        next_idx = end + 1
        while next_idx <= len(lines):
            if lines[next_idx - 1].strip():
                next_line = lines[next_idx - 1].strip()
                break
            next_idx += 1
        mermaid_blocks.append({
            'start': start,
            'end': end,
            'code': ''.join(code_lines),
            'next_line': next_line,
            'next_line_num': next_idx
        })
        start = None
    elif start is not None:
        code_lines.append(line)

print(f"Total Mermaid blocks found: {len(mermaid_blocks)}")
for i, b in enumerate(mermaid_blocks, 1):
    print(f"\n--- Mermaid Block #{i} (Lines {b['start']}..{b['end']}) ---")
    print(f"Followed by line {b['next_line_num']}: \"{b['next_line']}\"")
