TOKEN = "7650751450:AAEQam6YE-1e-mvedLjLhWVAmUQ79RSfzJc"
URL = 'https://tg-game-e8uu.vercel.app/'

import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo
import asyncio


bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start — запуск мини-приложения
@dp.message(CommandStart())
async def start_game(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🚀 Играть", web_app=WebAppInfo(url=URL))]
        ],
        resize_keyboard=True
    )
    await message.answer("Нажми кнопку ниже, чтобы запустить игру:", reply_markup=kb)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


