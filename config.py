import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ADMIN_ID = int(os.getenv("ADMIN_ID"))  # твой айди
TARGET_DATE = (2026, 6, 1)  # К чему считаем (ГОД, МЕСЯЦ, ДЕНЬ)