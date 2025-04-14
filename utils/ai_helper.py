import openai

openai.api_key = "YOUR_API_KEY"  # Load via env in production

def ask_ai_about_logs(text, question):
    prompt = f"Given the following sysdiagnose log:\n\n{text}\n\nAnswer this question:\n{question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message["content"]
