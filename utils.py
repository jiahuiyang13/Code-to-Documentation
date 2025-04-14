import os

# === Read full script ===
def read_full_script(file_path):
    """Reads the entire contents of a Python file."""
    if not os.path.isfile(file_path):
        print(f"[Error] File not found: {file_path}")
        return ""

    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"[Error] Couldn't read the file: {e}")
        return ""

# === Save to Markdown ===
def save_to_markdown(code, documentation, prompt, output_dir="docs", file_index=1):
    """Saves the code, documentation, and prompt to a Markdown file."""
    os.makedirs(output_dir, exist_ok=True)

    filename = f"script_{file_index}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(f"# Script Documentation ({filename})\n\n")

        f.write("## Original Code\n")
        f.write("```python\n")
        f.write(code)
        f.write("\n```\n\n")

        f.write("## Generated Documentation\n")
        f.write(documentation)
        f.write("\n\n")

        f.write("## Prompt Used\n")
        f.write("```\n")
        f.write(prompt)
        f.write("\n```")

    print(f"✅ Saved to {filepath}")

def read_full_script(file_path):
    if not os.path.isfile(file_path):
        print(f"[Error] File not found: {file_path}")
        return ""

    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"[Error] Couldn't read the file: {e}")
        return ""
