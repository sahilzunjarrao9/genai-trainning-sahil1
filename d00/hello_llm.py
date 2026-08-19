import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()  # reads OPENAI_API_KEY from the environment

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user",
               "content": "Say hello to a new AI engineering trainee in one sentence."}],
)
print(resp.choices[0].message.content)

