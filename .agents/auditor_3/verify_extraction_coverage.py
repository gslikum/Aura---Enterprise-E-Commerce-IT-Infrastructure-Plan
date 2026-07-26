import os
import re

AGENTS_DIR = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/.agents"
NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    master_notes = f.read()

batches = [
    ("Batch 1 (Img 1-22)", os.path.join(AGENTS_DIR, "worker_batch_1", "extracted_batch_1.md")),
    ("Batch 2 (Img 23-44)", os.path.join(AGENTS_DIR, "worker_batch_2", "extracted_batch_2.md")),
    ("Batch 3 (Img 45-66)", os.path.join(AGENTS_DIR, "worker_batch_3", "extracted_batch_3.md")),
    ("Batch 4 (Img 67-86)", os.path.join(AGENTS_DIR, "worker_batch_4", "extracted_batch_4.md"))
]

for label, batch_path in batches:
    print(f"\n================ {label} ================")
    if not os.path.exists(batch_path):
        print(f"File not found: {batch_path}")
        continue
    with open(batch_path, "r", encoding="utf-8") as bf:
        b_content = bf.read()
    
    # Find all Image N headers in batch file
    img_headers = re.findall(r"##\s*Image\s*(\d+)", b_content, re.IGNORECASE)
    print(f"Images extracted in {label}: {img_headers}")
    
    # Sample key terms/headings from batch file to check if present in master notes
    sub_headers = re.findall(r"###+\s*(.*)", b_content)
    print(f"Total sub-headings in batch: {len(sub_headers)}")
    missing_items = []
    for sh in sub_headers[:10]:
        clean_sh = sh.strip().replace("#", "").strip()
        # check if key words from sub-heading are in master_notes
        words = [w for w in re.split(r"\W+", clean_sh) if len(w) > 4]
        found = any(w.lower() in master_notes.lower() for w in words)
        if not found:
            missing_items.append(clean_sh)
    
    if missing_items:
        print(f"Potentially missing sub-headings: {missing_items}")
    else:
        print("Sampled sub-headings matched in master notes.")

