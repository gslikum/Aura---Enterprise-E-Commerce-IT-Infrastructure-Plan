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

print("=== DEEP MERMAID LABEL & EDGE ANALYSIS ===")

# Node labels are enclosed in brackets: [], (), {}, [[ ]], [( )], [/ /], [\ \], etc.
# Edge labels are enclosed in ||: |label|

# Regex matching node declarations with shapes
node_regex = re.compile(r'\b[A-Za-z0-9_]+\s*(?:\[\[|\[\(|\[/|\[\\|\[|\{|\()(?:"([^"]+)"|([^\]\}\)\n]+))(?:\]\]|\)\]|/\]|\\\]|\]|\}|\))')
edge_labels_regex = re.compile(r'\|([^|\n]+)\|')

num_prefix = re.compile(r'^\s*\d+[\.\)]\s+')
bullet_prefix = re.compile(r'^\s*[\u2022\*\-\+]\s+|\u2022')

node_violations = []
edge_violations = []
all_node_labels = []

for i, block in enumerate(mermaid_blocks, 1):
    for line_num, line_str in block['lines']:
        # Extract node labels
        node_matches = node_regex.findall(line_str)
        for q_val, unq_val in node_matches:
            val = q_val if q_val else unq_val
            val_strip = val.strip()
            all_node_labels.append((i, line_num, val_strip))
            if num_prefix.match(val_strip) or bullet_prefix.search(val_strip):
                node_violations.append((i, line_num, val_strip))
        
        # Extract edge labels
        edge_matches = edge_labels_regex.findall(line_str)
        for edge_val in edge_matches:
            edge_strip = edge_val.strip()
            if num_prefix.match(edge_strip) or bullet_prefix.search(edge_strip):
                edge_violations.append((i, line_num, edge_strip))

print(f"Total node labels scanned: {len(all_node_labels)}")
print(f"Node Label Violations (list numbering or bullets inside node [...] / (...) / {...}): {len(node_violations)}")
for v in node_violations:
    print(f"  Block #{v[0]}, Line {v[1]}: \"{v[2]}\"")

print(f"\nEdge/Link Label Violations (list numbering or bullets inside |...|): {len(edge_violations)}")
for v in edge_violations:
    print(f"  Block #{v[0]}, Line {v[1]}: \"{v[2]}\"")

