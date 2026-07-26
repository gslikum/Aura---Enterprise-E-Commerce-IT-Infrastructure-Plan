target_file = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/Chapter_5_Notes.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- BLOCK 7 LINES (337-362) ---")
for idx in range(336, 362):
    print(f"Line {idx+1}: {repr(lines[idx])}")

print("\n--- BLOCK 8 LINES (407-438) ---")
for idx in range(406, 438):
    print(f"Line {idx+1}: {repr(lines[idx])}")
