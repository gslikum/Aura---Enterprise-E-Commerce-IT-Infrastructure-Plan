import re

# Read Chapter_5_Notes.md
with open('/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md', 'r') as f:
    content = f.read()

# Find all mermaid blocks
pattern = r'```mermaid\s*\n(.*?)\n```'
blocks = re.findall(pattern, content, re.DOTALL)

print(f"Found {len(blocks)} Mermaid blocks.")

for i, block in enumerate(blocks, 1):
    lines = block.strip().split('\n')
    header = lines[0].strip()
    print(f"\n--- Block {i} (Header: {header}) ---")
    print(block)
