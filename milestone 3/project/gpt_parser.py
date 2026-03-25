from openai import OpenAI
client = OpenAI()

def parse_with_gpt(text):
    prompt = f"""
    You are a medical diet assistant.

    Extract diet-related instructions from this note.
    Return JSON with:
    - condition
    - diet_rules (list)

    Note:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
