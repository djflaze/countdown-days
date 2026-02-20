from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import date

from config import BOT_TOKEN, ADMIN_ID, TARGET_DATE
from storage import get_data, update_phrase, add_user
from ai import generate_phrase


def days_left():
    target = date(*TARGET_DATE)
    return (target - date.today()).days


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    data = get_data()
    today = str(date.today())

    d_left = days_left()

    if data["phrase_date"] != today:
        phrase = generate_phrase(d_left)
        update_phrase(phrase)
    else:
        phrase = data["phrase_text"]

    await update.message.reply_text(
        f"⏳ Осталось дней: {d_left}\n\n{phrase}"
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    data = get_data()
    await update.message.reply_text(
        f"👤 Пользователей: {len(data['users'])}\n"
        f"🗓 Фраза от: {data['phrase_date']}"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))

    app.run_polling()


if __name__ == "__main__":
    main()
