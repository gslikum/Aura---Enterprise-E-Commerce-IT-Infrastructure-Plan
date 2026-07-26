import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

print("--- Image / Page / Figure Mentions ---")
matches = re.findall(r"(?:image|page|figure|screenshot)\s*\d+", content, re.IGNORECASE)
print(f"Total image/page/figure/screenshot matches: {len(matches)}")
print(set(matches[:30]))

print("\n--- Searching for 'Image' in content ---")
img_matches = re.findall(r".{0,50}image.{0,50}", content, re.IGNORECASE)
print(f"Total 'image' mentions: {len(img_matches)}")
for m in img_matches[:10]:
    print("  MATCH:", m.strip())

print("\n--- Check document structure / Headings ---")
headings = re.findall(r"^(#+ .*)$", content, re.MULTILINE)
print(f"Total headings: {len(headings)}")
for h in headings[:25]:
    print("  ", h)

