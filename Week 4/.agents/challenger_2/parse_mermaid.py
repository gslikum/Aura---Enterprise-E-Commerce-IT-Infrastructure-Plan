import re
import sys

target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

def extract_blocks(lines):
    blocks = []
    in_b = False
    s_line = 0
    cur = []
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("```mermaid"):
            if in_b:
                print(f"Error: unclosed block before line {idx}")
            in_b = True
            s_line = idx
            cur = []
        elif line.strip() == "```" and in_b:
            in_b = False
            blocks.append((s_line, idx, cur))
            cur = []
        elif in_b:
            cur.append((idx, line))
    return blocks

blocks = extract_blocks(lines)
print(f"Extracted {len(blocks)} blocks.\n")

VALID_DIAGRAM_TYPES = [
    "graph", "flowchart", "sequenceDiagram", "classDiagram", "stateDiagram",
    "stateDiagram-v2", "erDiagram", "gantt", "pie", "gitGraph", "timeline",
    "mindmap", "quadrantChart", "sankey-beta", "xychart-beta", "block-beta"
]

VALID_DIRECTIONS = ["TD", "TB", "BT", "RL", "LR"]

def validate_block(block_num, start_l, end_l, content_lines):
    issues = []
    print(f"=== Validating Block {block_num} (Lines {start_l}-{end_l}) ===")
    
    if not content_lines:
        issues.append("Empty Mermaid code block")
        return issues
        
    first_line_num, first_line = content_lines[0]
    first_line_str = first_line.strip()
    tokens = first_line_str.split()
    
    dtype = tokens[0] if tokens else ""
    if dtype not in VALID_DIAGRAM_TYPES:
        issues.append(f"Line {first_line_num}: Invalid diagram type '{dtype}'")
    
    if dtype in ["graph", "flowchart"]:
        if len(tokens) < 2:
            issues.append(f"Line {first_line_num}: Missing orientation for '{dtype}' (expected TD, LR, etc.)")
        elif tokens[1] not in VALID_DIRECTIONS:
            issues.append(f"Line {first_line_num}: Invalid orientation '{tokens[1]}' for '{dtype}'")
            
    # Subgraph balance & syntax check
    subgraph_stack = []
    
    # Arrow pattern checks
    # Known invalid arrow patterns:
    # <.-.-> (invalid dotted bidirectional arrow, should be <-.->)
    # <===> (3 equal signs bidirectional, standard is <==>)
    
    for lno, ltext in content_lines:
        s_line = ltext.strip()
        if not s_line or s_line.startswith("%%"):
            continue
            
        # Check subgraphs
        if s_line.startswith("subgraph"):
            subgraph_stack.append((lno, s_line))
            # Validate subgraph line format:
            # Valid: subgraph ID [Title], subgraph ID ["Title"], subgraph "Title", subgraph ID
            sg_rest = s_line[8:].strip()
            # Check for unquoted spaces without brackets: e.g. "subgraph Center Hub"
            if " " in sg_rest and not ("[" in sg_rest or '"' in sg_rest or "'" in sg_rest):
                issues.append(f"Line {lno}: Invalid subgraph declaration '{s_line}'. Title with spaces must be quoted or enclosed in brackets, e.g. subgraph Center_Hub [Center Hub] or subgraph \"Center Hub\".")
                
        elif s_line == "end" or s_line.startswith("end "):
            if not subgraph_stack:
                issues.append(f"Line {lno}: Unexpected 'end' without matching 'subgraph'")
            else:
                subgraph_stack.pop()

        # Check arrow syntax errors
        if "<.-.->" in s_line:
            issues.append(f"Line {lno}: Invalid arrow syntax '<.-.->'. Dot after '<' is invalid syntax; should be '<-.->'.")
        if "<===>" in s_line:
            issues.append(f"Line {lno}: Non-standard arrow syntax '<===>'. Standard thick bidirectional arrow is '<==>'.")
        if "<===>" in s_line or "<--->" in s_line:
            pass # We check length extensions
            
        # Check bracket balancing in line
        # Paired: [], (), {}, ""
        # Note: (( )) or [( )] or [[ ]]
        square_b = 0
        paren_b = 0
        curly_b = 0
        dquote_b = 0
        
        in_dquote = False
        for c in s_line:
            if c == '"':
                in_dquote = not in_dquote
            elif not in_dquote:
                if c == '[': square_b += 1
                elif c == ']': square_b -= 1
                elif c == '(': paren_b += 1
                elif c == ')': paren_b -= 1
                elif c == '{': curly_b += 1
                elif c == '}': curly_b -= 1
                
        if in_dquote:
            issues.append(f"Line {lno}: Unmatched double quote in line: {s_line}")
        if square_b != 0:
            issues.append(f"Line {lno}: Unbalanced square brackets [] in line: {s_line}")
        if paren_b != 0:
            issues.append(f"Line {lno}: Unbalanced parentheses () in line: {s_line}")
        if curly_b != 0:
            issues.append(f"Line {lno}: Unbalanced curly brackets {{}} in line: {s_line}")
            
    if subgraph_stack:
        for lno, sg in subgraph_stack:
            issues.append(f"Line {lno}: Unclosed subgraph '{sg}'")
            
    return issues

all_issues = {}
for i, (s_l, e_l, c_lines) in enumerate(blocks, 1):
    issues = validate_block(i, s_l, e_l, c_lines)
    all_issues[i] = issues

print("\n================ SUMMARY OF FINDINGS ================")
total_errors = 0
for i, issues in all_issues.items():
    if issues:
        print(f"\nBlock {i}: {len(issues)} ISSUE(S) FOUND:")
        for iss in issues:
            print(f"  - {iss}")
            total_errors += 1
    else:
        print(f"Block {i}: PASSED (0 issues)")

print(f"\nTotal Issues Found across all blocks: {total_errors}")
