import re

# Read Chapter_5_Notes.md
with open('/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md', 'r') as f:
    content = f.read()

pattern = r'```mermaid\s*\n(.*?)\n```'
blocks = re.findall(pattern, content, re.DOTALL)

def check_block(idx, code):
    lines = code.strip().split('\n')
    diag_type = lines[0].strip()
    errors = []
    warnings = []

    print(f"=== Block {idx}: {diag_type} ===")

    # Check for specific invalid tokens
    for l_num, line in enumerate(lines, 1):
        s_line = line.strip()
        if not s_line:
            continue
        
        # Check arrows in graph/flowchart
        if 'graph' in diag_type or 'flowchart' in diag_type:
            # Check suspicious arrow formats like <.-.->
            if '<.-.->' in s_line:
                errors.append(f"Line {l_num}: Invalid link token '<.-.->' in '{s_line}'. Valid dotted bidirectional link in Mermaid is '<-.->'.")
            
            # Check subgraph declarations
            if s_line.startswith('subgraph'):
                # Check subgraph format
                # Valid formats:
                # subgraph ID [Title]
                # subgraph ID ["Title"]
                # subgraph "Title"
                # subgraph ID
                m = re.match(r'^subgraph\s+([^\s\["]+)(\s+.*)?$', s_line)
                if m:
                    sub_id = m.group(1)
                    rest = m.group(2)
                    if rest:
                        rest = rest.strip()
                        if not (rest.startswith('[') and rest.endswith(']')) and not (rest.startswith('"') and rest.endswith('"')):
                            warnings.append(f"Line {l_num}: Subgraph declaration '{s_line}' uses unquoted title with spaces ('{rest}'). Recommended format: `subgraph ID [Title]` or `subgraph ID [\"Title\"]` to avoid parsing ambiguity.")
                
            # Check bracket matching
            open_sq = s_line.count('[')
            close_sq = s_line.count(']')
            if open_sq != close_sq:
                errors.append(f"Line {l_num}: Mismatched square brackets in '{s_line}' ({open_sq} open vs {close_sq} close)")

            open_paren = s_line.count('(')
            close_paren = s_line.count(')')
            if open_paren != close_paren:
                errors.append(f"Line {l_num}: Mismatched parentheses in '{s_line}' ({open_paren} open vs {close_paren} close)")

            # Check quote matching
            quotes = s_line.count('"')
            if quotes % 2 != 0:
                errors.append(f"Line {l_num}: Mismatched double quotes in '{s_line}' ({quotes} quotes)")

    print(f"Errors found: {len(errors)}")
    for e in errors:
        print(f"  CRITICAL ERROR: {e}")
    print(f"Warnings found: {len(warnings)}")
    for w in warnings:
        print(f"  WARNING: {w}")

for i, block in enumerate(blocks, 1):
    check_block(i, block)
