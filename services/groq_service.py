import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_subtasks(task):
    prompt = (
        f"You are a productivity assistant. "
        f"Break the following task into exactly 3 concise and actionable subtasks. "
        f"Only return a numbered list, no introductions, explanations, or extra text.\n"
        f"Task: {task}" 
    )
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=150
    )
    raw = response.choices[0].message.content.strip().split("\n")
    return [s.strip("1234567890. ") for s in raw if s.strip()]

def translate_task(task, language):
    prompt = (
        f"Translate the following task into {language}. "
        f"Return only the exact or best translation. Do not include explanations, alternatives, or extra text. "
        f"Only reply with the translated task:\n\n"
        f"Task: {task}"
    )
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()
