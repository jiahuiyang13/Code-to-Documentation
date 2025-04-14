import os
import csv
import sys

# 👇 Add this block before importing from utils
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PARENT_DIR)

from utils import read_full_script

REPO_DIR = "./code_doc_dataset/repos"
OUTPUT_CSV = "./code_doc_dataset/data/scripts_dataset.csv"

rows = []

# Loop through all .py files
for root, _, files in os.walk(REPO_DIR):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            print(f"📄 Reading: {file_path}")

            code = read_full_script(file_path)
            if code:
                relative_path = os.path.relpath(file_path, REPO_DIR)
                rows.append({
                    "filename": relative_path,
                    "code": code.strip()
                })

# Save to CSV
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["filename", "code"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"\n✅ Saved {len(rows)} scripts to {OUTPUT_CSV}")
