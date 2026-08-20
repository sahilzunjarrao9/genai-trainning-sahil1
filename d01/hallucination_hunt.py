import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

questions = [
    "What is the capital of Maharashtra?",
    "Who wrote the Ramayana?",
    "What are the annual charges of the Platinum Sapphire Credit Card from SuryaFirst Bank?",
    "What are the current RBI repo rate and today's date?",
    "What is the customer-care number of SuryaFirst Bank?"
]

for question in questions:
    print("\n" + "=" * 60)
    print("QUESTION:", question)

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("ANSWER:", response.choices[0].message.content)