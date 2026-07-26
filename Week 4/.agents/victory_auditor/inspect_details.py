import os
import re

notes_path = '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md'

with open(notes_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("=== 1. GLOSSARY SECTION INSPECTION ===")
glossary_idx = content.find("## Glossary of Key Terms")
appendix_idx = content.find("## 2026 Appendix")

if glossary_idx != -1:
    glossary_text = content[glossary_idx:appendix_idx] if appendix_idx != -1 else content[glossary_idx:]
    print("Glossary raw snippet (first 1500 chars):\n")
    print(glossary_text[:1500])
    
    # Count terms in table or bold terms
    bold_terms = re.findall(r'\*\*(.*?)\*\*', glossary_text)
    print(f"\nTotal bold terms in Glossary section: {len(bold_terms)}")

print("\n=== 2. MERMAID DIAGRAMS FULL CONTENT ===")
blocks = content.split('```')
mermaid_blocks = []
for i in range(1, len(blocks), 2):
    block = blocks[i]
    if block.startswith('mermaid'):
        mermaid_blocks.append(block[7:].strip())

for idx, m in enumerate(mermaid_blocks, 1):
    print(f"\n--- DIAGRAM {idx} ---")
    print(m)

print("\n=== 3. CASE STUDY QUESTIONS & ANSWERS DETAILS ===")
cs_idx = content.find("## Case Study Questions & Answers")
cs_text = content[cs_idx:glossary_idx] if glossary_idx != -1 else content[cs_idx:]
print(f"Case study section length: {len(cs_text)} chars, {len(cs_text.splitlines())} lines")

q_matches = re.findall(r'\*\*Question\s*\d+:\*\*', cs_text)
print(f"Explicit Question headers count: {len(q_matches)}")
for q in q_matches[:10]:
    print("  ", q)

