import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find all Case Study headings
cs_matches = re.finditer(r"##\s*Case\s+Study\s+\d+:\s*(.*)", content)

for match in cs_matches:
    title = match.group(1)
    start = match.start()
    # Find end of this case study (next ## Case Study or next ## Key Terms Glossary)
    next_match = re.search(r"\n##\s+", content[start + 20:])
    if next_match:
        end = start + 20 + next_match.start()
    else:
        end = len(content)
    
    cs_block = content[start:end]
    print(f"\n==================================================")
    print(f"CASE STUDY: {title}")
    print(f"==================================================")
    
    # Check Case Context
    has_context = "### Case Context" in cs_block
    print(f"Case Context section present: {has_context}")
    
    # Extract Questions
    questions = re.findall(r"####\s*(Question\s*\d+:.*?)(?=\n####|\n##|\Z)", cs_block, re.DOTALL)
    print(f"Total Questions found: {len(questions)}")
    
    for idx, q_text in enumerate(questions, 1):
        q_lines = q_text.strip().splitlines()
        q_header = q_lines[0]
        q_body = "\n".join(q_lines[1:])
        
        # Count paragraphs in answer (non-empty blocks)
        paragraphs = [p for p in q_body.split("\n\n") if p.strip()]
        word_count = len(re.findall(r"\w+", q_body))
        
        print(f"\n  [{q_header[:70]}...]")
        print(f"    Paragraph count: {len(paragraphs)}")
        print(f"    Word count: {word_count}")

