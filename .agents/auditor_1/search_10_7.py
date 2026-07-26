import re

file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Search for '10.7':")
matches_10_7 = [m.start() for m in re.finditer(r'10\.7', text)]
print(f"Found {len(matches_10_7)} occurrences of '10.7'.")

print("\nSearch for 'career':")
matches_career = [(m.start(), text[max(0, m.start()-50):min(len(text), m.end()+100)]) for m in re.finditer(r'career', text, re.IGNORECASE)]
for idx, (pos, snippet) in enumerate(matches_career, 1):
    print(f"{idx}. pos {pos}: {snippet!r}")
