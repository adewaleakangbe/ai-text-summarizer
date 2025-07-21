from openai import OpenAI
from config import OPENAI_API_KEY, DEFAULT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text: str, model: str = DEFAULT_MODEL) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes long texts."},
                {"role": "user", "content": f"Summarize this:\n{text}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
