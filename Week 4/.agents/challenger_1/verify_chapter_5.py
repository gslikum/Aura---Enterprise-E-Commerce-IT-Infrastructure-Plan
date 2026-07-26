import os
import re
import sys

TARGET_FILE = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

def test_file_exists():
    assert os.path.exists(TARGET_FILE), f"File non-existent: {TARGET_FILE}"
    print(f"[PASS] File exists: {TARGET_FILE}")

def analyze_headings(content):
    headings = re.findall(r'^(#{1,6})\s+(.+)$', content, flags=re.MULTILINE)
    print(f"\n--- HEADING HIERARCHY ANALYSIS ---")
    print(f"Total Headings Found: {len(headings)}")
    
    h1_count = len([h for h in headings if len(h[0]) == 1])
    h2_count = len([h for h in headings if len(h[0]) == 2])
    h3_count = len([h for h in headings if len(h[0]) == 3])
    h4_count = len([h for h in headings if len(h[0]) == 4])
    
    print(f"H1: {h1_count}, H2: {h2_count}, H3: {h3_count}, H4+: {h4_count}")
    
    heading_titles = [h[1].strip() for h in headings]
    
    # Required core sections
    required_keywords = [
        "Infrastructure",
        "Hardware",
        "Software",
        "Data Management",
        "Network", # or Telecommunications
        "Cloud",
        "Case Study",
        "Glossary", # or Key Terms
        "2026 Appendix" # or Emerging
    ]
    
    missing_topics = []
    for kw in required_keywords:
        found = any(kw.lower() in title.lower() for title in heading_titles)
        if found:
            print(f"  [PASS] Found heading matching required topic '{kw}'")
        else:
            print(f"  [FAIL] Missing heading matching required topic '{kw}'")
            missing_topics.append(kw)
            
    return headings, missing_topics

def analyze_2026_appendix(content):
    print(f"\n--- 2026 APPENDIX SHIFTS ANALYSIS ---")
    # Find 2026 Appendix section
    appendix_match = re.search(r'#{1,4}\s+.*2026 Appendix.*', content, flags=re.IGNORECASE)
    if not appendix_match:
        print("  [FAIL] 2026 Appendix heading not found!")
        return False
    
    appendix_text = content[appendix_match.start():]
    
    shifts = {
        "19 state privacy laws with 2026 dates": False,
        "SECURE Data Act 2026 (H.R. 8413)": False,
        "EU AI Act Article 50 (watermarking)": False,
        "Generative AI copyright litigation": False
    }
    
    # 1. 19 state laws with 2026 dates
    if re.search(r'19\s+state', appendix_text, re.I) and re.search(r'2026', appendix_text):
        shifts["19 state privacy laws with 2026 dates"] = True
    elif re.search(r'state\s+privacy\s+laws', appendix_text, re.I) and re.search(r'19', appendix_text):
        shifts["19 state privacy laws with 2026 dates"] = True
        
    # 2. SECURE Data Act 2026 H.R. 8413
    if ("SECURE" in appendix_text or "H.R. 8413" in appendix_text or "8413" in appendix_text):
        shifts["SECURE Data Act 2026 (H.R. 8413)"] = True
        
    # 3. EU AI Act Art 50 watermarking
    if ("EU AI Act" in appendix_text or "Article 50" in appendix_text or "Art. 50" in appendix_text or "Art 50" in appendix_text) and ("watermark" in appendix_text.lower() or "provenance" in appendix_text.lower()):
        shifts["EU AI Act Article 50 (watermarking)"] = True
        
    # 4. GenAI copyright litigation
    if ("copyright" in appendix_text.lower() or "litigation" in appendix_text.lower() or "fair use" in appendix_text.lower()) and ("genai" in appendix_text.lower() or "generative" in appendix_text.lower() or "ai" in appendix_text.lower()):
        shifts["Generative AI copyright litigation"] = True

    all_passed = True
    for shift_name, status in shifts.items():
        if status:
            print(f"  [PASS] {shift_name} detected in Appendix")
        else:
            print(f"  [FAIL] {shift_name} NOT detected in Appendix")
            all_passed = False
            
    return all_passed

def analyze_glossary(content):
    print(f"\n--- GLOSSARY COMPLETENESS ANALYSIS ---")
    glossary_match = re.search(r'#{1,4}\s+.*(Glossary|Key Terms).*', content, flags=re.IGNORECASE)
    if not glossary_match:
        print("  [FAIL] Glossary section not found!")
        return []
    
    glossary_text = content[glossary_match.start():]
    # Check terms defined in glossary
    glossary_entries = re.findall(r'^\s*[-*]\s*\*\*([^*]+)\*\*', glossary_text, flags=re.MULTILINE)
    if not glossary_entries:
        glossary_entries = re.findall(r'^\s*\|?\s*\*\*([^*]+)\*\*\s*\|', glossary_text, flags=re.MULTILINE)
    if not glossary_entries:
        glossary_entries = re.findall(r'^\s*#{3,5}\s+(.+)$', glossary_text, flags=re.MULTILINE)
        
    print(f"  Glossary entries count: {len(glossary_entries)}")
    for g in glossary_entries[:10]:
        print(f"    - {g}")
    if len(glossary_entries) > 10:
        print(f"    ... and {len(glossary_entries) - 10} more.")
        
    return glossary_entries

def analyze_publication_grade(content):
    print(f"\n--- PUBLICATION GRADE LENGTH & DETAIL ANALYSIS ---")
    lines = content.splitlines()
    words = content.split()
    chars = len(content)
    
    print(f"  Total Lines: {len(lines)}")
    print(f"  Total Words: {len(words)}")
    print(f"  Total Characters: {chars}")
    
    # Check mermaid diagrams
    mermaid_blocks = re.findall(r'```mermaid', content)
    print(f"  Mermaid Diagrams Count: {len(mermaid_blocks)}")
    
    # Check tables
    tables = re.findall(r'^\s*\|.*\|', content, flags=re.MULTILINE)
    print(f"  Table Lines Count: {len(tables)}")
    
    # Check code blocks / lists
    bullet_items = re.findall(r'^\s*[-*]\s+', content, flags=re.MULTILINE)
    print(f"  Bullet Points Count: {len(bullet_items)}")

    is_pub_grade = (
        len(words) >= 3000 and
        len(mermaid_blocks) >= 1 and
        len(lines) >= 500
    )
    print(f"  Publication Grade Assessment: {'PASS' if is_pub_grade else 'FAIL'}")
    return is_pub_grade

def main():
    test_file_exists()
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    headings, missing_headings = analyze_headings(content)
    appendix_ok = analyze_2026_appendix(content)
    glossary_terms = analyze_glossary(content)
    pub_grade_ok = analyze_publication_grade(content)
    
    print("\n================ SUMMARY ================")
    print(f"Headings Check: {'PASS' if not missing_headings else 'FAIL'}")
    print(f"2026 Appendix Check: {'PASS' if appendix_ok else 'FAIL'}")
    print(f"Glossary Check: {'PASS' if len(glossary_terms) >= 10 else 'FAIL'} ({len(glossary_terms)} terms)")
    print(f"Publication Grade Check: {'PASS' if pub_grade_ok else 'FAIL'}")

if __name__ == "__main__":
    main()
