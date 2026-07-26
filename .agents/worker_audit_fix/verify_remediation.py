import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

# Find all mermaid blocks
mermaid_blocks = []
in_block = False
start_idx = 0
block_lines = []

for idx, line in enumerate(lines):
    if line.strip() == "```mermaid":
        in_block = True
        start_idx = idx
        block_lines = []
    elif in_block and line.strip() == "```":
        in_block = False
        end_idx = idx
        mermaid_blocks.append((start_idx, end_idx, block_lines))
    elif in_block:
        block_lines.append((idx + 1, line))

print(f"=== VERIFICATION AUDIT REPORT ===")
print(f"Total Mermaid blocks found: {len(mermaid_blocks)} (Expected: 12)")
assert len(mermaid_blocks) == 12, f"Expected 12 blocks, found {len(mermaid_blocks)}"

# Check 1: List syntax in node labels or edge labels
list_syntax_patterns = [
    r'•',
    r'^\s*\d+[\.\)]', # 1. or 1)
    r'<br\s*/?>\s*•',
    r'<br\s*/?>\s*\d+[\.\)]',
    r'\|\s*\d+[\.\)]', # |1. or |1) in edge labels
    r'\[\s*\d+[\.\)]', # [1. in node strings
    r'\(\s*\d+[\.\)]', # (1. in node strings
    r'Click\s+\d+',
    r'Rule\s+\d+'
]

violations = []
for b_idx, (s, e, blines) in enumerate(mermaid_blocks, 1):
    for line_num, line_str in blines:
        for pat in list_syntax_patterns:
            if re.search(pat, line_str):
                violations.append((b_idx, line_num, line_str.strip(), pat))

print(f"\n--- CHECK 1: MERMAID LIST SYNTAX AUDIT ---")
print(f"Total violations found: {len(violations)}")
for v in violations:
    print(f"  [FAIL] Block #{v[0]} Line {v[1]}: {v[2]} (Matched: {v[3]})")

if len(violations) == 0:
    print("  [PASS] ZERO list syntax or numbered list prefixes found across all 12 Mermaid diagrams.")

# Check 2: Explanatory Breakdown headers and required components
print(f"\n--- CHECK 2: EXPLANATORY BREAKDOWN AUDIT ---")
breakdown_headers = []
required_keys = ["Inputs", "Core Processing Mechanisms", "Decisioning Logic", "Outputs"]

for b_idx, (s, e, blines) in enumerate(mermaid_blocks, 1):
    # Search following lines for Breakdown header
    found_header = None
    breakdown_text = ""
    for idx in range(e + 1, min(e + 30, len(lines))):
        l = lines[idx]
        if l.strip().startswith("## ") and not l.strip().startswith("### Explanatory Breakdown"):
            break
        if l.strip().startswith("### Explanatory Breakdown of Figure 10."):
            found_header = l.strip()
            # gather breakdown text
            breakdown_text = "\n".join(lines[idx:min(idx+20, len(lines))])
            break
    
    print(f"Diagram #{b_idx} (Line {s+1}-{e+1}) -> Header: {found_header}")
    assert found_header is not None, f"Missing breakdown header for Diagram #{b_idx}"
    
    # Verify required components
    missing_keys = []
    for rk in required_keys:
        if rk not in breakdown_text:
            missing_keys.append(rk)
    
    if missing_keys:
        print(f"  [FAIL] Diagram #{b_idx} missing components: {missing_keys}")
    else:
        print(f"  [PASS] Diagram #{b_idx} contains all 4 mandatory components (Inputs, Core Processing, Decisioning Logic, Outputs).")

# Check 3: Section 10.7 Integration & Placement
print(f"\n--- CHECK 3: SECTION 10.7 INTEGRATION AUDIT ---")
sec_10_7_idx = -1
case_study_idx = -1

for i, l in enumerate(lines):
    if "## 10.7 How Will MIS Help My Career?" in l:
        sec_10_7_idx = i
    elif "# Case Study Questions & Answers" in l:
        case_study_idx = i

print(f"Section 10.7 found at line: {sec_10_7_idx + 1}")
print("Case Study Questions & Answers found at line:", case_study_idx + 1)
assert sec_10_7_idx != -1, "Section 10.7 is missing!"
assert case_study_idx != -1, "Case Study section is missing!"
assert sec_10_7_idx < case_study_idx, "Section 10.7 must appear BEFORE Case Study Questions & Answers!"

print("  [PASS] Section 10.7 is fully integrated and correctly positioned before Case Study Questions & Answers.")
