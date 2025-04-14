from utils.ai_helper import ask_ai_about_logs

def generate_summary(full_text):
    summary_prompt = "Summarize key events and activity from this iOS sysdiagnose log."
    return ask_ai_about_logs(full_text, summary_prompt)
