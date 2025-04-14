import sys
import os
import json

# Add parent directory to the path so we can import from generator.py and utils.py
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PARENT_DIR)

from generator import create_script_documentation_prompt, generate_documentation
from utils import read_full_script

REPO_DIR = "./code_doc_dataset/repos"
OUTPUT_PATH = "./code_doc_dataset/data/code_doc_dataset.json"

dataset = []

# Loop through all Python files in all repositories
for root, _, files in os.walk(REPO_DIR):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            print(f"📄 Processing: {file_path}")

            try:
                script = read_full_script(file_path)
                if script:
                    prompt = create_script_documentation_prompt(script)
                    doc = generate_documentation(prompt)
                    dataset.append({
                        "input": script.strip(),
                        "output": doc.strip()
                    })
            except Exception as e:
                print(f"⚠️ Error processing {file_path}: {e}")

# Save all input/output pairs into a JSON file
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2)

print(f"\n✅ Done! Saved {len(dataset)} script samples to {OUTPUT_PATH}")
