import re

file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split('\n')

print("=== DEEP CHECK 1: CHEATING / SHORTCUTS / DUMMY TEXT / TRUNCATION ===")

# Check 1a: Empty sections / headings with no body text before next heading
empty_sections = []
for i in range(len(lines)):
    line = lines[i].strip()
    if line.startswith('#'):
        # look ahead for non-empty line before next heading
        has_content = False
        j = i + 1
        while j < len(lines):
            next_line = lines[j].strip()
            if next_line.startswith('#'):
                break
            if next_line and next_line != '---':
                has_content = True
                break
            j += 1
        if not has_content:
            empty_sections.append((i+1, line))

print(f"Empty headings count: {len(empty_sections)}")
for loc, sec in empty_sections:
    print(f"  Line {loc}: {sec}")

# Check 1b: Unmatched code blocks or unclosed tags
mermaid_starts = len(re.findall(r'```mermaid', text))
code_ends = len(re.findall(r'```', text))
print(f"Mermaid blocks: {mermaid_starts}, Total triple-backtick markers: {code_ends}")

if code_ends % 2 != 0:
    print("  FAIL: Unclosed code block detected!")

# Check 1c: Check for trailing ellipsis or unfinished sentences at section ends
unfinished = []
for i, l in enumerate(lines):
    l_str = l.strip()
    if l_str.endswith('...') or l_str.endswith('---...') or re.search(r'\[\s*\]', l_str):
        unfinished.append((i+1, l_str))

print(f"Potential unfinished/placeholder lines: {len(unfinished)}")
for loc, content in unfinished:
    print(f"  Line {loc}: {content}")

# Check 1d: Repeated identical paragraphs (copy-paste shortcuts)
paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 50 and not p.strip().startswith('```')]
unique_paragraphs = set(paragraphs)
if len(paragraphs) != len(unique_paragraphs):
    print(f"WARNING: Found {len(paragraphs) - len(unique_paragraphs)} duplicate paragraphs!")
else:
    print("PASS: No duplicate paragraphs detected.")
