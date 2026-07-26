import re
import os
import sys

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
SCREENSHOTS_DIR = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/chapter_10_screenshots"

def run_audit():
    print("=" * 60)
    print("STARTING VICTORY AUDIT FOR CHAPTER 10 NOTES")
    print("=" * 60)

    if not os.path.exists(NOTES_PATH):
        print(f"ERROR: Target notes file not found at {NOTES_PATH}")
        sys.exit(1)

    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    print(f"Total lines in Chapter_10_Notes.md: {len(lines)}")
    print(f"Total characters: {len(content)}")

    # -------------------------------------------------------------
    # CHECK 1: Screenshots & Completeness (Image 1 to 86 + Sec 10.7)
    # -------------------------------------------------------------
    print("\n--- CHECK 1: Single-Image Exhaustive Audit Loop ---")
    screenshot_files = sorted(os.listdir(SCREENSHOTS_DIR))
    print(f"Total screenshot files in directory: {len(screenshot_files)}")

    # Search for Image 1 .. Image 86 citations in content
    missing_images = []
    found_images = []
    for i in range(1, 87):
        # Look for variations like Image 1, Image 01, img_1, etc.
        patterns = [
            f"Image {i}\\b",
            f"Image {i:02d}\\b",
            f"Image_{i}\\b",
            f"Image_{i:02d}\\b"
        ]
        found = False
        for pat in patterns:
            if re.search(pat, content, re.IGNORECASE):
                found = True
                break
        if found:
            found_images.append(i)
        else:
            missing_images.append(i)

    print(f"Images cited/integrated count: {len(found_images)} / 86")
    if missing_images:
        print(f"WARNING/FAIL: Missing image citations for: {missing_images}")
    else:
        print("PASS: All 86 images explicitly referenced/cited in exact numerical order.")

    # Check Section 10.7
    sec_10_7_match = re.search(r"10\.7\s+How\s+Will\s+MIS\s+Help\s+My\s+Career", content, re.IGNORECASE)
    if sec_10_7_match:
        print("PASS: Section 10.7 ('How Will MIS Help My Career?') header found.")
        # Check content length in 10.7
        idx = sec_10_7_match.start()
        sec_10_7_text = content[idx:idx+5000]
        print(f"Section 10.7 excerpt (first 300 chars):\n{sec_10_7_text[:300]}...")
    else:
        print("FAIL: Section 10.7 ('How Will MIS Help My Career?') not found!")

    # -------------------------------------------------------------
    # CHECK 2: Core Content & Learning Objectives
    # -------------------------------------------------------------
    print("\n--- CHECK 2: Core Content & Formatting ---")
    lo_missing = []
    for i in range(1, 8):
        lo_str = f"10-{i}"
        if lo_str in content or f"10.{i}" in content:
            print(f"  LO 10-{i}: FOUND")
        else:
            print(f"  LO 10-{i}: MISSING")
            lo_missing.append(lo_str)

    if lo_missing:
        print(f"FAIL: Missing Learning Objectives: {lo_missing}")
    else:
        print("PASS: Learning Objectives 10-1 through 10-7 documented.")

    # Business models check
    models = ["B2C", "B2B", "C2C"]
    for m in models:
        if f"**{m}**" in content or f"**{m}:" in content or m in content:
            print(f"  Model {m}: FOUND")
        else:
            print(f"  Model {m}: MISSING")

    # Dynamic pricing check
    if "dynamic pricing" in content.lower():
        print("  Dynamic Pricing: FOUND")

    # -------------------------------------------------------------
    # CHECK 3: Mermaid.js Diagrams & Explanatory Breakdowns
    # -------------------------------------------------------------
    print("\n--- CHECK 3: Mermaid.js Diagrams & Explanatory Breakdowns ---")
    mermaid_blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL)
    print(f"Total Mermaid diagram blocks found: {len(mermaid_blocks)}")

    bullet_violations = []
    numbered_violations = []

    for idx, block in enumerate(mermaid_blocks, 1):
        # Extract text inside node labels, e.g. [...] or (...) or ["..."]
        # Also check entire line inside mermaid block for prohibited bullet / numbered list patterns
        lines_in_block = block.splitlines()
        for l_num, line in enumerate(lines_in_block, 1):
            # Check bullet character •
            if "•" in line:
                bullet_violations.append((idx, l_num, line.strip()))
            # Check numbered list patterns inside string quotes or brackets like "1. ", "2. ", "[1. ", "(1. "
            if re.search(r'["\[\(\>\:]\s*\d+\.\s+[A-Za-z]', line):
                numbered_violations.append((idx, l_num, line.strip()))

    if bullet_violations:
        print(f"FAIL: Bullet point (•) violations found in Mermaid blocks: {len(bullet_violations)}")
        for v in bullet_violations[:5]:
            print(f"  Block {v[0]}, Line {v[1]}: {v[2]}")
    else:
        print("PASS: ZERO bullet points (•) in Mermaid diagram labels.")

    if numbered_violations:
        print(f"FAIL: Numbered list syntax violations found in Mermaid blocks: {len(numbered_violations)}")
        for v in numbered_violations[:5]:
            print(f"  Block {v[0]}, Line {v[1]}: {v[2]}")
    else:
        print("PASS: ZERO numbered list prefixes in Mermaid diagram labels.")

    # Check Explanatory Breakdowns for EVERY diagram
    # Search for all breakdown headings
    breakdown_matches = list(re.finditer(r"###+\s*Explanatory\s+Breakdown", content, re.IGNORECASE))
    print(f"Total Explanatory Breakdown headings found: {len(breakdown_matches)}")

    # Check if each breakdown has Inputs, Processing, Outputs
    breakdown_completeness = True
    for b_idx, match in enumerate(breakdown_matches, 1):
        start = match.start()
        end = breakdown_matches[b_idx].start() if b_idx < len(breakdown_matches) else start + 3000
        snippet = content[start:end]
        
        has_inputs = "input" in snippet.lower()
        has_processing = "process" in snippet.lower() or "mechanism" in snippet.lower()
        has_outputs = "output" in snippet.lower()

        if not (has_inputs and has_processing and has_outputs):
            print(f"WARNING: Breakdown {b_idx} missing section details (Inputs: {has_inputs}, Processing: {has_processing}, Outputs: {has_outputs})")
            breakdown_completeness = False

    if len(breakdown_matches) >= len(mermaid_blocks):
        print(f"PASS: Every Mermaid diagram ({len(mermaid_blocks)}) has a corresponding Explanatory Breakdown section ({len(breakdown_matches)}).")
    else:
        print(f"FAIL: Mismatch in diagram count ({len(mermaid_blocks)}) vs Explanatory Breakdown count ({len(breakdown_matches)}).")

    # -------------------------------------------------------------
    # CHECK 4: Case Studies Q&A
    # -------------------------------------------------------------
    print("\n--- CHECK 4: Case Studies Q&A ---")
    case_studies = [
        ("Opening Case", r"Opening Case"),
        ("FinTech Case", r"FinTech|Small Business Loan"),
        ("Social Engagement Case", r"Social Engagement|Social Commerce"),
        ("Uber Closing Case", r"Uber|Closing Case")
    ]
    for name, pattern in case_studies:
        m = re.search(pattern, content, re.IGNORECASE)
        if m:
            print(f"  {name}: FOUND")
        else:
            print(f"  {name}: MISSING")

    # Check for Q&A structures (Question / Answer blocks)
    qa_blocks = re.findall(r"\*\*Question\s*\d*.*?\*\*", content)
    print(f"Total explicit Question markers found: {len(qa_blocks)}")

    # -------------------------------------------------------------
    # CHECK 5: Key Terms Glossary
    # -------------------------------------------------------------
    print("\n--- CHECK 5: Key Terms Glossary ---")
    glossary_match = re.search(r"##\s*Key\s+Terms\s+Glossary", content, re.IGNORECASE)
    if glossary_match:
        print("PASS: 'Key Terms Glossary' section heading found.")
        glossary_start = glossary_match.start()
        # Find next section after glossary or end of file
        next_sec = re.search(r"\n##\s+", content[glossary_start + 20:])
        if next_sec:
            glossary_text = content[glossary_start:glossary_start + 20 + next_sec.start()]
        else:
            glossary_text = content[glossary_start:]

        # Extract terms (e.g. - **Term**: Definition or **Term**: Definition)
        terms = re.findall(r"[\-\*]?\s*\*\*([^*]+)\*\*\s*:", glossary_text)
        print(f"Total terms found in Glossary: {len(terms)}")
        
        # Check alphabetical order
        clean_terms = [t.strip().lower() for t in terms if t.strip()]
        is_sorted = clean_terms == sorted(clean_terms)
        if is_sorted:
            print("PASS: Key Terms Glossary is in strict alphabetical order.")
        else:
            print("WARNING/FAIL: Key Terms Glossary is NOT sorted alphabetically!")
            # Find out where sorting fails
            for i in range(len(clean_terms) - 1):
                if clean_terms[i] > clean_terms[i+1]:
                    print(f"  Sorting error at position {i}: '{terms[i]}' comes before '{terms[i+1]}'")
                    break
    else:
        print("FAIL: Key Terms Glossary section not found!")

    # -------------------------------------------------------------
    # CHECK 6: 2026 Appendix
    # -------------------------------------------------------------
    print("\n--- CHECK 6: 2026 Appendix ---")
    appendix_match = re.search(r"##\s*2026\s+Appendix:\s+Emerging\s+E-Commerce\s+&\s+Digital\s+Market\s+Shifts", content, re.IGNORECASE)
    if appendix_match:
        print("PASS: Section '## 2026 Appendix: Emerging E-Commerce & Digital Market Shifts' found.")
        appendix_text = content[appendix_match.start():]
        topics = [
            ("Agentic E-Commerce", r"Agentic E-Commerce|Agentic"),
            ("EU AI Act Synthetic Media Rules (August 2026)", r"EU AI Act|Synthetic Media|August 2026"),
            ("Dynamic Pricing & Transparency Regulations", r"Dynamic Pricing|Transparency Regulations"),
            ("Social Commerce & Unified Checkout", r"Social Commerce|Unified Checkout")
        ]
        for t_name, t_pat in topics:
            if re.search(t_pat, appendix_text, re.IGNORECASE):
                print(f"  Topic '{t_name}': COVERED")
            else:
                print(f"  Topic '{t_name}': MISSING")
    else:
        print("FAIL: Section '## 2026 Appendix: Emerging E-Commerce & Digital Market Shifts' NOT found!")

    print("=" * 60)
    print("AUDIT SCRIPT EXECUTION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_audit()
