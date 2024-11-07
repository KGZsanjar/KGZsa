import asyncio
import random
from bot_config import bot, dp
from handlers.start import start_router
from aiogram.filters import Command

from setuptools.extern import names

# @dp.message(Command(""))
# async def picture_handler(message: types.Message):
#     message.text
#     photo = types.FSInputFile("")


@dp.message()
async def echo_handler(message: type.Message):
    await message.reply(message.text)


async def main():
    dp.include_router(start_router)


@dp.message(Command("myinfo"))
async def myinfo_handler(message: type.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username or "Не указан"

    msg = f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш юзернейм: {username}"
    await message.answer(msg)



async def main():
    await dp.start_polling(bot)


if names == 'main':
    asyncio.run(main())


