import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../.env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# Read complaint from complaint.txt
with open("complaint.txt", "r", encoding="utf-8") as file:
    complaint = file.read()


# -------------------------
# Prompt A - Bad / Simple
# -------------------------

prompt_a = f"""
Summarize this email:

{complaint}
"""


# -------------------------
# Prompt B - Structured
# -------------------------

prompt_b = f"""
You are a complaints triage assistant for a bank.

Analyze the following customer complaint.

Return exactly three fields:

issue
severity: low|medium|high
requested_action

Rules:
- Only use information from the email.
- Do not invent details.
- Severity must be exactly one of: low, medium, high.

Email:
{complaint}
"""


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Run both prompts
output_a = ask_ai(prompt_a)
output_b = ask_ai(prompt_b)


# Print results
print("\n========== PROMPT A ==========\n")
print(output_a)

print("\n========== PROMPT B ==========\n")
print(output_b)
