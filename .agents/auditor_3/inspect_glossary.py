import re

NOTES_PATH = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_10_Notes.md"

with open(NOTES_PATH, "r", encoding="utf-8") as f:
    content = f.read()

glossary_match = re.search(r"##\s*Key\s+Terms\s+Glossary", content, re.IGNORECASE)
if not glossary_match:
    print("Glossary not found!")
    exit(1)

glossary_start = glossary_match.start()
next_sec = re.search(r"\n##\s+", content[glossary_start + 20:])
if next_sec:
    glossary_text = content[glossary_start:glossary_start + 20 + next_sec.start()]
else:
    glossary_text = content[glossary_start:]

terms = re.findall(r"[\-\*]?\s*\*\*([^*]+)\*\*\s*:", glossary_text)
print(f"Glossary contains {len(terms)} terms:\n")
for idx, term in enumerate(terms, 1):
    print(f"{idx:02d}. {term}")

print("\n--- Checking Alphabetic Sorting ---")
# 1) Natural / Case-insensitive letter-only sort
def normalize_term(t):
    # Remove parens and non-alphanumeric except space
    return re.sub(r"[^a-zA-Z0-9\s]", "", t).lower().strip()

norm_terms = [normalize_term(t) for t in terms]

sorted_norm = sorted(norm_terms)

out_of_order = []
for i in range(len(norm_terms) - 1):
    if norm_terms[i] > norm_terms[i+1]:
        out_of_order.append((i, terms[i], norm_terms[i], terms[i+1], norm_terms[i+1]))

print(f"\nTotal out-of-order pairs (letter-only lowercased): {len(out_of_order)}")
for o in out_of_order:
    print(f"  Pos {o[0]+1}: '{o[1]}' ('{o[2]}') > '{o[3]}' ('{o[4]}')")

# 2) Standard str.lower() sort
str_lower_terms = [t.lower() for t in terms]
sorted_str_lower = sorted(str_lower_terms)

out_of_order_lower = []
for i in range(len(str_lower_terms) - 1):
    if str_lower_terms[i] > str_lower_terms[i+1]:
        out_of_order_lower.append((i, terms[i], terms[i+1]))

print(f"\nTotal out-of-order pairs (standard str.lower()): {len(out_of_order_lower)}")
for o in out_of_order_lower:
    print(f"  Pos {o[0]+1}: '{o[1]}' > '{o[2]}'")

