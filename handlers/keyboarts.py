from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Перейти на сайт instagram", url="https://www.instagram.com/invites/contact/?"))
    keyboard.add(InlineKeyboardButton("Связаться с нами", url="igsh=42d4l03m61x2&utm_content=q9yxefp"))
    return keyboard

# Telegram ("https://t.me/DEWWISTy")
# Onni Bernström