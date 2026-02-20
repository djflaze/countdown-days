from aiogram import Bot, Dispatcher, executor, types
from datetime import date
from config import BOT_TOKEN, TARGET_DATE, ADMIN_ID
from db import can_send, users_count
from ai import generate_phrase

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def days_left():
    target = date(*TARGET_DATE)
    return (target - date.today()).days

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not can_send(message.from_user.id):
        await message.answer("Сегодня ты уже получал фразу 🙂")
        return

    days = days_left()
    phrase = generate_phrase(days)

    await message.answer(
        f"До лета осталось {days} дней.\n\n{phrase}"
    )

@dp.message_handler(commands=["stats"])
async def stats(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(f"👤 Пользователей: {users_count()}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)