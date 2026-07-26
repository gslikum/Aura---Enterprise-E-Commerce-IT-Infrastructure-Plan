import os
import re

notes_path = '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md'
screenshots_dir = '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/chapter_5_screenshots'

with open(notes_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("=========================================")
print("   VICTORY AUDIT DETAILED CHECK SCRIPT   ")
print("=========================================\n")

# Check 1: File Existence & Metrics
print("--- 1. FILE METRICS ---")
print(f"File path: {notes_path}")
print(f"File exists: {os.path.exists(notes_path)}")
print(f"File size: {os.path.getsize(notes_path)} bytes")
print(f"Line count: {len(content.splitlines())}")
print(f"Word count: {len(content.split())}")

# Check 2: Learning Objectives
print("\n--- 2. LEARNING OBJECTIVES ---")
lo_header = "## Learning Objectives" in content
lo_count = len(re.findall(r'Learning Objective 5-\d:', content))
print(f"Learning Objectives header present: {lo_header}")
print(f"Learning Objectives count (LO 5-1 to 5-6): {lo_count}")

# Check 3: Mermaid Diagrams
print("\n--- 3. MERMAID DIAGRAMS ---")
blocks = content.split('```')
mermaid_blocks = []
for i in range(1, len(blocks), 2):
    block = blocks[i]
    if block.startswith('mermaid'):
        mermaid_blocks.append(block[7:].strip())

print(f"Total Mermaid blocks found: {len(mermaid_blocks)}")
all_mermaid_valid = True
for idx, mb in enumerate(mermaid_blocks, 1):
    lines = [l for l in mb.splitlines() if l.strip()]
    if not lines:
        print(f"  Diagram {idx}: EMPTY (FAIL)")
        all_mermaid_valid = False
    else:
        diagram_type = lines[0]
        print(f"  Diagram {idx}: {diagram_type} ({len(lines)} lines)")
        # basic syntax sanity check
        valid_starts = ('graph', 'flowchart', 'sequenceDiagram', 'classDiagram', 'stateDiagram', 'gantt', 'pie', 'erDiagram', 'gitGraph')
        if not any(diagram_type.startswith(vs) for vs in valid_starts):
            print(f"    WARNING: Diagram {idx} has unusual start line: {diagram_type}")

# Check 4: Case Study Q&A
print("\n--- 4. CASE STUDY QUESTIONS & ANSWERS ---")
cs_header = "## Case Study Questions & Answers" in content
print(f"Case Study header present: {cs_header}")
case_studies = [
    "American Airlines Heads for the Cloud",
    "BYOD",
    "Look to the Cloud",
    "Dollar Rent A Car"
]
for cs in case_studies:
    present = cs in content
    print(f"  Case study '{cs}': {'PRESENT' if present else 'MISSING'}")

# Check 5: Glossary
print("\n--- 5. GLOSSARY OF KEY TERMS ---")
glossary_header = "## Glossary of Key Terms" in content
print(f"Glossary header present: {glossary_header}")
glossary_matches = re.findall(r'-\s+\*\*(.*?)\*\*:', content[content.find("## Glossary of Key Terms"):] if "## Glossary of Key Terms" in content else "")
print(f"Glossary terms count: {len(glossary_matches)}")

# Check 6: 2026 Appendix
print("\n--- 6. 2026 APPENDIX ---")
app_header = "## 2026 Appendix: Emerging Technological & Legal Shifts" in content
print(f"2026 Appendix header present: {app_header}")

app_reqs = {
    "19 active U.S. State Privacy Laws (Indiana, Kentucky, Rhode Island in 2026)": [
        "19", "Indiana", "Kentucky", "Rhode Island"
    ],
    "Federal IT compliance under SECURE Data Act of 2026 (H.R. 8413) data minimization": [
        "SECURE Data Act", "8413", "minimization"
    ],
    "EU AI Act August 2026 Article 50 transparency mandates (synthetic watermarking & AI disclosure)": [
        "EU", "Artificial Intelligence Act", "Article 50", "watermarking"
    ],
    "Multi-district copyright litigation concerning GenAI model training datasets": [
        "copyright", "GenAI", "training datasets"
    ]
}

for req_name, keywords in app_reqs.items():
    found_all = all(kw.lower() in content.lower() for kw in keywords)
    print(f"  Req '{req_name}': {'PASS' if found_all else 'FAIL'}")
    for kw in keywords:
        print(f"    - '{kw}': {'FOUND' if kw.lower() in content.lower() else 'MISSING'}")

# Check 7: Screenshot Coverage Analysis
print("\n--- 7. SCREENSHOT COVERAGE ---")
screenshot_files = sorted([f for f in os.listdir(screenshots_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))])
print(f"Total screenshot files in directory: {len(screenshot_files)}")

# Check batch raw files and notes to see how screenshots were processed and covered
explorer_batches = [
    '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/.agents/explorer_1/batch_1_raw.md',
    '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/.agents/explorer_2/batch_2_raw.md',
    '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/.agents/explorer_3/batch_3_raw.md'
]

batch_content = ""
for b_path in explorer_batches:
    if os.path.exists(b_path):
        with open(b_path, 'r', encoding='utf-8') as f_b:
            batch_content += f_b.read() + "\n"

covered_in_batches = 0
for s in screenshot_files:
    if s in batch_content or s.replace('\u202f', ' ') in batch_content.replace('\u202f', ' '):
        covered_in_batches += 1

print(f"Screenshots transcribed in batch raw files: {covered_in_batches} / {len(screenshot_files)}")

# Check 8: Cheating / Placeholder Detection
print("\n--- 8. CHEATING / PLACEHOLDER DETECTION ---")
placeholders = ['TODO', 'TBD', 'Lorem ipsum', 'FIXME', 'XXX', '[INSERT', '[PLACEHOLDER']
found_ph = []
for ph in placeholders:
    matches = re.findall(rf'\b{re.escape(ph)}\b', content, re.IGNORECASE)
    if matches:
        found_ph.append((ph, len(matches)))

print(f"Placeholders detected: {found_ph if found_ph else 'ZERO (PASS)'}")

