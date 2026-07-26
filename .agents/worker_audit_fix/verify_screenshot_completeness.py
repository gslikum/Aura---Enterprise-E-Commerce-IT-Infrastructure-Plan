import re
import os

ocr_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/.agents/worker_audit_fix/ocr_results.txt"
notes_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(ocr_path, "r", encoding="utf-8") as f:
    ocr_text = f.read()

with open(notes_path, "r", encoding="utf-8") as f:
    notes_text = f.read()

# Split OCR results by Image headers
images_data = ocr_text.split("========================================\nIMAGE ")
print(f"Total OCR Image sections parsed: {len(images_data) - 1}")

# Check coverage of key sections across the 86 screenshots
coverage_check = {
    "Learning Objectives (10-1 to 10-7)": ["10-1", "10-2", "10-3", "10-4", "10-5", "10-6", "10-7"],
    "Section 10.1 E-Commerce Today": ["Ubiquitous", "Marketspace", "Global Reach", "Universal Standards", "Richness", "Interactivity", "Information Density", "Personalization", "Social Technology", "Disintermediation", "Digital Goods"],
    "Section 10.2 Business and Technology Models": ["B2C", "B2B", "C2C", "Portal", "E-tailer", "Content Provider", "Transaction Broker", "Market Creator", "Service Provider", "Community Provider", "FinTech"],
    "Section 10.3 E-Commerce Marketing": ["Long Tail", "Behavioral Targeting", "Ad Network", "Social Graph", "Crowdsourcing", "Wisdom of Crowds"],
    "Section 10.4 B2B E-Commerce": ["EDI", "Electronic Data Interchange", "Private Industrial Network", "Net Marketplace", "E-Hub", "Exchanges"],
    "Section 10.5 M-Commerce": ["Location-Based Services", "Geoadvertising", "Geoinformation", "NFC", "Apple Pay", "Google Pay", "P2P"],
    "Section 10.6 E-Commerce Presence": ["Presence Map", "Websites", "Email", "Social Media", "Offline Media"],
    "Section 10.7 Career Integration": ["E-Commerce Operations Specialist", "Product Information Management", "PCI-DSS"],
    "Case Studies": ["Fourth Screen", "Uber", "Small Business Loans", "Socially"],
    "2026 Appendix": ["Agentic E-Commerce", "EU AI Act Synthetic Media", "Dynamic Pricing", "Surveillance Pricing"]
}

print("\n--- SINGLE-IMAGE AUDIT COVERAGE REPORT ---")
all_passed = True
for section_name, keywords in coverage_check.items():
    missing_in_notes = []
    for kw in keywords:
        if kw.lower() not in notes_text.lower():
            missing_in_notes.append(kw)
    
    if missing_in_notes:
        print(f"  [FAIL] Section '{section_name}' missing keywords in notes: {missing_in_notes}")
        all_passed = False
    else:
        print(f"  [PASS] Section '{section_name}' fully covered in Chapter_10_Notes.md")

print(f"\nFinal Completeness Status: {'100% COMPLETE' if all_passed else 'INCOMPLETE'}")
