import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

breakdown_matches = list(re.finditer(r"###\s*Explanatory\s+Breakdown\s+of\s+Figure\s+(\d+\.\d+):\s*(.*)", content))

print(f"Total Explanatory Breakdown sections found: {len(breakdown_matches)}\n")

for idx, match in enumerate(breakdown_matches, 1):
    fig_num = match.group(1)
    fig_title = match.group(2)
    start_pos = match.start()
    
    # End position is next header or line 20 lines down
    next_hdr = re.search(r"\n#+\s+", content[start_pos + 10:])
    if next_hdr:
        end_pos = start_pos + 10 + next_hdr.start()
    else:
        end_pos = start_pos + 2000
        
    bd_text = content[start_pos:end_pos]
    
    has_inputs = any(w in bd_text.lower() for w in ["input", "data stream", "ingestion", "source", "feed"])
    has_processing = any(w in bd_text.lower() for w in ["process", "mechanism", "transformation", "logic", "algorithm", "routing", "calculation", "underwriting", "analytics"])
    has_outputs = any(w in bd_text.lower() for w in ["output", "result", "disbursement", "display", "decision", "action", "delivery"])
    
    print(f"[{idx:02d}] Figure {fig_num}: {fig_title}")
    print(f"     Inputs: {has_inputs} | Processing: {has_processing} | Outputs: {has_outputs}")
    print("     First 150 chars:", repr(bd_text[:150]))
    print()

