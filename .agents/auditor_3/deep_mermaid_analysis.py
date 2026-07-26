import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find all mermaid blocks and their preceding/following headings
mermaid_matches = list(re.finditer(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL))

print(f"Total Mermaid diagrams found: {len(mermaid_matches)}\n")

for idx, match in enumerate(mermaid_matches, 1):
    block_str = match.group(1)
    start_pos = match.start()
    end_pos = match.end()
    
    # Preceding heading
    preceding_text = content[:start_pos]
    preceding_headings = re.findall(r"(#+\s*.*)", preceding_text)
    last_heading = preceding_headings[-1] if preceding_headings else "N/A"
    
    # Following heading
    following_text = content[end_pos:]
    following_headings = re.findall(r"(#+\s*.*)", following_text)
    next_heading = following_headings[0] if following_headings else "N/A"
    
    print(f"--- Diagram #{idx} ---")
    print(f"  Preceding heading: {last_heading}")
    print(f"  Next heading:      {next_heading}")
    
    # Check node labels
    # Regex to find text inside [...], (...), {...}, [[...]], [(...)]
    node_labels = re.findall(r"[\(\[\{\>]\s*\"?([^\n\"\]\)\}]+)\"?\s*[\)\]\}]", block_str)
    
    bullet_violations = []
    number_violations = []
    
    for nl in node_labels:
        if "•" in nl:
            bullet_violations.append(nl)
        # Check for 1., 2., 1), 2) at start of node string label
        if re.match(r"^\s*\d+[\.\)]\s+", nl):
            number_violations.append(nl)
            
    print(f"  Total node labels extracted: {len(node_labels)}")
    print(f"  Bullet violations: {len(bullet_violations)} {bullet_violations}")
    print(f"  Number list violations: {len(number_violations)} {number_violations}")
    
    # Check if next heading is Explanatory Breakdown
    is_breakdown = "Explanatory Breakdown" in next_heading
    print(f"  Followed immediately by Explanatory Breakdown: {is_breakdown}")
    
    # Inspect content of the breakdown section
    if is_breakdown:
        # Get text of breakdown
        breakdown_text = following_text.split("```")[0].split("\n##")[0]
        has_inputs = "input" in breakdown_text.lower()
        has_processing = "process" in breakdown_text.lower() or "mechanism" in breakdown_text.lower()
        has_outputs = "output" in breakdown_text.lower()
        print(f"  Breakdown details -> Inputs: {has_inputs}, Processing: {has_processing}, Outputs: {has_outputs}")
    print()

