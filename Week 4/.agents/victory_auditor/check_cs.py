import os

notes_path = '/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md'

with open(notes_path, 'r', encoding='utf-8') as f:
    content = f.read()

cs_idx = content.find("## Case Study Questions & Answers")
glossary_idx = content.find("## Glossary of Key Terms")

cs_text = content[cs_idx:glossary_idx]
print(cs_text[:4000])
