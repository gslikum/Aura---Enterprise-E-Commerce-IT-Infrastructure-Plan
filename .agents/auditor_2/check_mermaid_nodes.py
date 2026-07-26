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
        mermaid_blocks.append({
            'start': start,
            'end': end,
            'lines': code_lines[:]
        })
        start = None
    elif start is not None:
        code_lines.append((idx, line))

print(f"Total Mermaid blocks found: {len(mermaid_blocks)}")

# Patterns for labels in Mermaid
# Node labels appear inside brackets like [...], ("..."), ("..."), {...}, [[...]], [(...)], [/.../], etc.
# String labels can be quoted ("...") or unquoted [...].

# We want to extract content inside node shapes: [], (), {}, [""], (""), etc.
node_label_regex = re.compile(r'(\[\[|\[\(|\[/|\[\\|\[|\{|\()(?:"([^"]+)"|([^\]\}\)\n]+))(\]\]|\)\]|/\]|\\\]|\]|\}|\))')

numbering_prefix_regex = re.compile(r'^\s*(?:\d+[\.\)]|\d+\.\d+|\u2022|\*|-|\+)\s+')
any_bullet_regex = re.compile(r'[\u2022\u2023\u25e6\u2043\u2219]')

violations = []

for i, block in enumerate(mermaid_blocks, 1):
    print(f"\n=================== MERMAID BLOCK #{i} (Lines {block['start']}..{block['end']}) ===================")
    for line_num, line_str in block['lines']:
        stripped = line_str.strip()
        if not stripped or stripped.startswith('flowchart') or stripped.startswith('graph') or stripped.startswith('sequenceDiagram') or stripped.startswith('subgraph') or stripped == 'end' or stripped.startswith('style') or stripped.startswith('classDef') or stripped.startswith('class ') or stripped.startswith('linkStyle'):
            print(f"Line {line_num}: {stripped}")
            continue
        
        print(f"Line {line_num}: {stripped}")
        
        # Find all brackets / labels in this line
        # Also let's extract strings inside brackets
        # Let's extract any text inside brackets/parens/braces that define nodes
        matches = node_label_regex.findall(line_str)
        for open_bracket, quoted_val, unquoted_val, close_bracket in matches:
            label_text = quoted_val if quoted_val else unquoted_val
            label_text = label_text.strip()
            
            # Check for list numbering prefix (e.g., "1.", "2.", "3.", "1)", "1.1", etc.)
            has_numbering = bool(re.match(r'^\s*\d+[\.\)]\s+', label_text) or re.match(r'^\s*\d+\.\d+\s+', label_text))
            has_bullet = bool(any_bullet_regex.search(label_text) or re.match(r'^\s*[\u2022\*\-\+]\s+', label_text))
            
            # Let's also check if there is numbering ANYWHERE in the string label as a prefix or bullet
            if has_numbering or has_bullet:
                violations.append({
                    'block': i,
                    'line_num': line_num,
                    'line_str': stripped,
                    'label': label_text,
                    'has_numbering': has_numbering,
                    'has_bullet': has_bullet
                })

print("\n=================== CHECK 2 VIOLATIONS ===================")
if violations:
    print(f"FAILED: Found {len(violations)} label violation(s):")
    for v in violations:
        print(f"  Block #{v['block']}, Line {v['line_num']}: label=\"{v['label']}\" (Numbering: {v['has_numbering']}, Bullet: {v['has_bullet']})")

