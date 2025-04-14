import requests
from utils import read_full_script, save_to_markdown

# === Constants ===
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "llama2"  # You can use "phi" or "mistral" for faster inference


# === Create prompt for full script ===
def create_script_documentation_prompt(script_code):
    """Creates a prompt to document a full Python script using LLM."""
    system_msg = "You are a helpful assistant that documents Python scripts clearly and concisely."

    user_msg = f"""
Please generate high-quality documentation for the following Python script.

- Provide a brief description of what the script does overall.
- Add inline comments or markdown-style section explanations.
- Highlight any API usage, GUI elements, or data logic.
- Format output in markdown, using code blocks where appropriate.

Script:
{script_code}
"""

    return f"System: {system_msg}\nUser: {user_msg}\nAssistant:"


# === Send prompt to Ollama ===
def generate_documentation(prompt, model=MODEL, temperature=0.2):
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_API_URL, json=payload)
        if res.status_code == 200:
            return res.json()["response"]
        else:
            return f"[Error] Ollama API responded with {res.status_code}: {res.text}"
    except Exception as e:
        return f"[Error] Exception while connecting to Ollama: {e}"


# === Main execution (for testing manually) ===
if __name__ == "__main__":
    path = "examples/sample_code.py"  # You can change this to any file
    script_code = read_full_script(path)

    if not script_code:
        print("⚠️ No code found or file could not be read.")
    else:
        print("✅ File read successfully. Sending to LLM...")

        prompt = create_script_documentation_prompt(script_code)
        doc = generate_documentation(prompt)

        print(f"\n--- Generated Script Documentation ---\n{doc}")
        save_to_markdown(script_code, doc, prompt, output_dir="docs", file_index=1)
