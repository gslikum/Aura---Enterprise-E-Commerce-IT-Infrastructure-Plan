import re

file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== ALL HEADINGS ===")
for idx, line in enumerate(lines, 1):
    if line.strip().startswith('#'):
        print(f"Line {idx:3d}: {line.strip()}")
