import re
import sys

file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

content = "".join(lines)

print(f"Total lines: {len(lines)}")
print(f"Total characters: {len(content)}")

# --- Check 1: Cheating / Shortcuts / Dummy Text ---
cheating_terms = [
    r"lorem ipsum", r"todo", r"fixme", r"\btbd\b", r"\[insert", r"placeholder",
    r"dummy", r"fake summary", r"sample text", r"truncated", r"coming soon",
    r"draft text"
]

cheating_found = []
for idx, line in enumerate(lines, 1):
    for term in cheating_terms:
        if re.search(term, line, re.IGNORECASE):
            cheating_found.append((idx, line.strip(), term))

print("\n=== CHECK 1: CHEATING & SHORTCUTS ===")
if cheating_found:
    print(f"FAIL: Found {len(cheating_found)} potential cheating/shortcut instances:")
    for c in cheating_found:
        print(f"  Line {c[0]}: matches '{c[2]}' -> {c[1]}")
else:
    print("PASS: No dummy text, TODOs, or cheating patterns detected.")

# --- Check 2: Mermaid node label syntax for prohibited list characters ---
print("\n=== CHECK 2: MERMAID NODE LABELS FOR LIST CHARACTERS ===")

# Find all mermaid blocks
mermaid_block_regex = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)
mermaid_blocks = list(mermaid_block_regex.finditer(content))

print(f"Found {len(mermaid_blocks)} Mermaid blocks.")

label_regex = re.compile(r'(?:\[|\(|\{\{|\[\[|\[\(|\>)(.*?)(?:\]|\)|\}\}|\]\]|\)\>|\)\])')
# Also node labels in quotes like ["..."] or ["1. ..."]
node_def_regex = re.compile(r'\b[A-Za-z0-0_]+\s*(?:\[|\[\"|\(|\(\"|\{\{|\{\{\"|\>|\>\"|\[\[|\[\[\")(.*?)(?:\]|\"\]|\)|\"\)|\}\}|\"\}\}|\"\]\]|\"\]|\"\>)')

prohibited_list_patterns = [
    (r'•', "bullet character •"),
    (r'^\s*\d+\.\s', "numbered list prefix (e.g. 1., 2.)"),
    (r'^\s*-\s', "dash list prefix"),
    (r'^\s*\*\s', "asterisk list prefix"),
    (r'•', "bullet character"),
    (r'[\u2022\u2023\u25b6\u25c0\u25ba\u25c4\u25e6\u25aa\u25ab\u25cf]', "unicode bullet symbol")
]

mermaid_violations = []

for b_idx, block in enumerate(mermaid_blocks, 1):
    block_text = block.group(1)
    block_start_line = content[:block.start()].count('\n') + 1
    
    # Extract labels inside brackets/parentheses
    # Matches patterns like ID[Label], ID("Label"), ID{Label}, ID[[Label]], ID[(Label)]
    # We can match anything inside brackets after an identifier
    lines_in_block = block_text.split('\n')
    for l_num, l_str in enumerate(lines_in_block, 1):
        # find labels
        # match [...] or (...) or {{...}}
        matches = re.findall(r'\[+([^\]]+)\]+|\(+([^\)]+)\)+|\{\{([^\}]+)\}\}', l_str)
        for m in matches:
            label_text = next(item for item in m if item)
            # clean quotes if any
            clean_label = label_text.strip('"\' ')
            
            # Check for list characters
            # check bullet symbol
            if '•' in clean_label:
                mermaid_violations.append((block_start_line + l_num - 1, b_idx, clean_label, "Bullet character '•' in label"))
            
            # check numbered prefix like "1. ", "2. ", "10-1. "
            if re.search(r'^\s*\d+[\.\)]\s', clean_label):
                mermaid_violations.append((block_start_line + l_num - 1, b_idx, clean_label, "Numbered list prefix (e.g. 1., 2.) in label"))

if mermaid_violations:
    print(f"FAIL: Found {len(mermaid_violations)} Mermaid node label syntax violations:")
    for v in mermaid_violations:
        print(f"  Line {v[0]} (Block {v[1]}): {v[3]} -> '{v[2]}'")
else:
    print("PASS: All Mermaid node labels adhere to syntax rules (no prohibited list characters).")

# --- Check 3: Mermaid block followed by Explanatory Breakdown section ---
print("\n=== CHECK 3: MERMAID EXPLANATORY BREAKDOWN SECTIONS ===")

breakdown_violations = []

for b_idx, block in enumerate(mermaid_blocks, 1):
    block_end_pos = block.end()
    block_start_line = content[:block.start()].count('\n') + 1
    
    # Look at the text after the block up to the next mermaid block or 1000 characters
    after_text = content[block_end_pos:block_end_pos + 1500]
    
    # Check if "Explanatory Breakdown" or "Breakdown" heading appears shortly after
    # Let's inspect the lines immediately following
    after_lines = [line.strip() for line in after_text.split('\n') if line.strip()][:10]
    
    found_breakdown = False
    breakdown_title = ""
    for line in after_lines:
        if re.search(r'Explanatory Breakdown', line, re.IGNORECASE) or re.search(r'Diagram Breakdown', line, re.IGNORECASE):
            found_breakdown = True
            breakdown_title = line
            break
            
    if found_breakdown:
        print(f"  Block {b_idx} at line {block_start_line}: Followed by breakdown -> {breakdown_title}")
    else:
        breakdown_violations.append((b_idx, block_start_line, after_lines[:3]))
        print(f"  Block {b_idx} at line {block_start_line}: MISSING Explanatory Breakdown! Following text: {after_lines[:2]}")

if breakdown_violations:
    print(f"FAIL: {len(breakdown_violations)} Mermaid block(s) missing Explanatory Breakdown section.")
else:
    print("PASS: Every Mermaid diagram block is followed by an Explanatory Breakdown section.")

# --- Check 4: Completeness of Required Sections ---
print("\n=== CHECK 4: REQUIRED SECTIONS COMPLETENESS ===")

required_sections = [
    ("Learning Objectives", r'##\s*Learning Objectives'),
    ("Chapter Opening Case", r'##\s*Chapter Opening Case'),
    ("Section 10.1", r'##\s*10\.1'),
    ("Section 10.2", r'##\s*10\.2'),
    ("Section 10.3", r'##\s*10\.3'),
    ("Section 10.4", r'##\s*10\.4'),
    ("Section 10.5", r'##\s*10\.5'),
    ("Section 10.6", r'##\s*10\.6'),
    ("Section 10.7", r'##\s*10\.7'),
    ("Case Studies / Interactive Cases", r'Case'),
    ("Glossary", r'##\s*Glossary|##\s*Key Terms|##\s*Chapter Glossary'),
    ("2026 Appendix", r'##\s*2026 Appendix|##\s*Appendix.*2026')
]

section_results = {}
for name, pattern in required_sections:
    matches = list(re.finditer(pattern, content, re.IGNORECASE))
    section_results[name] = len(matches) > 0
    print(f"  {name}: {'FOUND (' + str(len(matches)) + ' matches)' if section_results[name] else 'MISSING'}")

missing_sections = [name for name, found in section_results.items() if not found]
if missing_sections:
    print(f"FAIL: Missing required sections: {missing_sections}")
else:
    print("PASS: All required major sections are present.")
