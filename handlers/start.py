from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()
unique_users = set()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    user_id = message.from_user.id
    unique_users.add(user_id)
    user_count = len(unique_users)
    msg = f"Привет, {name}, наш бот обслуживает уже {user_count} пользователя."
    # await message.answer(msg)
    # chat_id=message.from_user.id
    # text=msg,


