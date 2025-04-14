import streamlit as st
from generator import read_full_script, create_script_documentation_prompt, generate_documentation, save_to_markdown
import tempfile
import os

st.set_page_config(page_title="📄 Script-to-Doc Generator", layout="wide")
st.title("📄 Python Script Documentation Generator")

st.markdown("Upload a `.py` script or paste code below. We’ll generate complete documentation using an LLM (via Ollama).")

# === Input options ===
input_type = st.radio("Choose input method:", ("Upload Python File", "Paste Code"))

script_code = ""

if input_type == "Upload Python File":
    uploaded_file = st.file_uploader("Upload a .py file", type="py")
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        script_code = read_full_script(tmp_path)

elif input_type == "Paste Code":
    script_code = st.text_area("Paste your Python code here", height=300)

# === Generate button ===
if st.button("Generate Documentation"):
    if not script_code:
        st.warning("⚠️ Please upload a file or paste some code first.")
    else:
        st.success("✅ Generating documentation using Ollama...")

        prompt = create_script_documentation_prompt(script_code)
        doc = generate_documentation(prompt)

        st.markdown("### 🧾 Generated Documentation")
        st.markdown(doc)

        save_to_markdown(script_code, doc, prompt, output_dir="docs", file_index=1)
        st.success("✅ Documentation saved to `docs/script_1.md`")
