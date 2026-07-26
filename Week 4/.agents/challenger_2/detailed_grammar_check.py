import sys
import re

target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

def get_mermaid_blocks(lines):
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
    return blocks

blocks = get_mermaid_blocks(lines)

def analyze_block_details(b_num, s_line, e_line, content):
    print(f"\n==================================================")
    print(f"BLOCK {b_num} (Lines {s_line}-{e_line})")
    print(f"==================================================")
    
    code = [line for lno, line in content]
    
    # 1. Declaration check
    header = code[0].strip() if code else ""
    print(f"Declaration: '{header}'")
    
    # 2. Check each line for potential render-breaking bugs
    findings = []
    
    for lno, raw_line in content:
        line = raw_line.strip()
        if not line or line.startswith("%%"):
            continue
            
        # Check 1: <.-.-> vs <-.->
        if "<.-.->" in line:
            findings.append((lno, "CRITICAL", f"Invalid arrow syntax '<.-.->' in line: `{line}`. The dot '.' after '<' creates a syntax error in Mermaid parser. Correct syntax: `<-.->`."))

        # Check 2: subgraph with multiple unquoted words without id/brackets
        if line.startswith("subgraph"):
            parts = line.split(maxsplit=1)
            if len(parts) > 1:
                rest = parts[1].strip()
                # If there are spaces, check if quoted or has []
                if " " in rest:
                    if not (rest.startswith('"') and rest.endswith('"')) and not ("[" in rest and "]" in rest):
                        findings.append((lno, "HIGH", f"Malformed subgraph header `{line}`. Subgraph title containing spaces must be enclosed in quotes or use ID [Title] syntax, e.g. `subgraph Center_Hub [Center Hub]` or `subgraph \"Center Hub\"`."))

        # Check 3: <===> arrow syntax
        if "<===>" in line:
            findings.append((lno, "MEDIUM", f"Non-standard bidirectional thick arrow `<===>` in line: `{line}`. Standard Mermaid thick bidirectional arrow is `<==>`. Some parsers render `<===>` as an error or literal."))

        # Check 4: Unbalanced quotes/brackets
        # Check quotes
        quotes_count = line.count('"')
        if quotes_count % 2 != 0:
            findings.append((lno, "CRITICAL", f"Unbalanced double quotes ({quotes_count}) in line: `{line}`."))
            
        # Check brackets pairing
        # Count outside quotes
        in_q = False
        sq = 0
        pa = 0
        cur = 0
        for ch in line:
            if ch == '"':
                in_q = not in_q
            elif not in_q:
                if ch == '[': sq += 1
                elif ch == ']': sq -= 1
                elif ch == '(': pa += 1
                elif ch == ')': pa -= 1
                elif ch == '{': cur += 1
                elif ch == '}': cur -= 1
        if sq != 0:
            findings.append((lno, "HIGH", f"Unbalanced square brackets `[]` (delta={sq}) in line: `{line}`."))
        if pa != 0:
            findings.append((lno, "HIGH", f"Unbalanced parentheses `()` (delta={pa}) in line: `{line}`."))
        if cur != 0:
            findings.append((lno, "HIGH", f"Unbalanced curly braces `{{}}` (delta={cur}) in line: `{line}`."))

    if not findings:
        print("RESULT: VALID — No rendering bugs or syntax errors detected.")
    else:
        print(f"RESULT: {len(findings)} FINDING(S) DETECTED:")
        for lno, severity, msg in findings:
            print(f"  - [Line {lno}] [{severity}] {msg}")

for i, (s, e, content) in enumerate(blocks, 1):
    analyze_block_details(i, s, e, content)
