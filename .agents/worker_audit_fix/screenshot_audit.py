import os

dir_path = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/chapter_10_screenshots"
files = [f for f in os.listdir(dir_path) if f.endswith(".png")]

# Sort files by filename or modification time
files_sorted = sorted(files)

print(f"Total screenshots found: {len(files_sorted)}")
for idx, fname in enumerate(files_sorted, 1):
    fpath = os.path.join(dir_path, fname)
    size = os.path.getsize(fpath)
    mtime = os.path.getmtime(fpath)
    print(f"Image {idx:02d}: {fname} ({size} bytes)")
