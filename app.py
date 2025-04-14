import streamlit as st
from utils.extract_sysdiagnose import extract_sysdiagnose, extract_zip_sysdiagnose
from utils.ai_helper import ask_ai_about_logs
from utils.visualization import plot_battery_usage
from utils.summary import generate_summary
import os

st.set_page_config(page_title="SYS Diagnose for iOS", layout="wide")
st.title("📱 SYS Diagnose for iOS")

option = st.sidebar.radio("Navigate", ["View Raw Data", "Use AI", "Visualization", "AI Summary"])

# Accept .tar.gz and .zip
uploaded_file = st.file_uploader("Upload sysdiagnose file (.tar.gz or .zip)", type=['gz', 'tar.gz', 'zip'])

if uploaded_file:
    file_path = f"./uploaded/{uploaded_file.name}"
    os.makedirs("./uploaded", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    extract_path = None

    if uploaded_file.name.endswith(".tar.gz"):
        extract_path = extract_sysdiagnose(file_path)
    elif uploaded_file.name.endswith(".zip"):
        extract_path = extract_zip_sysdiagnose(file_path)
    else:
        st.error("Unsupported file format.")

    if extract_path:
        if option == "View Raw Data":
            st.subheader("📂 File Explorer")
            for root, _, files in os.walk(extract_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith(".log") or file.endswith(".txt"):
                        with open(file_path, "r", errors='ignore') as f:
                            content = f.read()
                        with st.expander(file):
                            st.text_area("Content", content[:3000], height=300)

        elif option == "Use AI":
            st.subheader("🤖 Ask AI About Logs")
            question = st.text_input("Enter your question")
            if st.button("Ask"):
                full_text = ""
                for root, _, files in os.walk(extract_path):
                    for file in files:
                        if file.endswith(".log") or file.endswith(".txt"):
                            with open(os.path.join(root, file), "r", errors='ignore') as f:
                                full_text += f.read()[:2000]
                answer = ask_ai_about_logs(full_text, question)
                st.success(answer)

        elif option == "Visualization":
            st.subheader("📈 Device Usage Trends")
            data = [{"timestamp": f"2025-04-1{i}", "battery_level": 100 - i*5} for i in range(10)]
            plot_battery_usage(data)

        elif option == "AI Summary":
            st.subheader("🧠 AI Summary")
            full_text = ""
            for root, _, files in os.walk(extract_path):
                for file in files:
                    if file.endswith(".log") or file.endswith(".txt"):
                        with open(os.path.join(root, file), "r", errors='ignore') as f:
                            full_text += f.read()[:2000]
            summary = generate_summary(full_text)
            st.write(summary)
