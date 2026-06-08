import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_input, memories):
    context = "\n".join(memories)

    prompt = f"""
You are an intelligent assistant with memory.

Past relevant memories:
{context}

User input:
{user_input}

Give a helpful and context-aware response.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
