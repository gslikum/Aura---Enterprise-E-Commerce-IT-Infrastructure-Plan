import re

path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

# Extract all H1, H2, H3, H4 headers and Mermaid blocks in order
for i, line in enumerate(lines, 1):
    if line.startswith("#"):
        print(f"Line {i:4d}: {line}")
    elif line.strip() == "```mermaid":
        print(f"Line {i:4d}: [MERMAID BLOCK START]")
