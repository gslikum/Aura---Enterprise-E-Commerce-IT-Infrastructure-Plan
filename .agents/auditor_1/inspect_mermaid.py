import re

file_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

mermaid_block_regex = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)
mermaid_blocks = list(mermaid_block_regex.finditer(text))

print(f"=== ALL {len(mermaid_blocks)} MERMAID BLOCKS ===")

for idx, block in enumerate(mermaid_blocks, 1):
    block_start_line = text[:block.start()].count('\n') + 1
    block_text = block.group(1)
    print(f"\n--- BLOCK {idx} (Line {block_start_line}) ---")
    print(block_text.strip())
