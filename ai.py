from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_phrase(days_left: int) -> str:
    prompt = f"""
    Придумай короткую, спокойную, немного философскую фразу
    про ожидание события.
    Осталось {days_left} дней.
    Без пафоса. Без мотивационных клише.
    1–2 предложения.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()