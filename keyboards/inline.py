from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_kb():
    send_photo = InlineKeyboardButton(text = "📸 Отправить фото", callback_data="send_photo")
    links = InlineKeyboardButton(text = "👥 Наш канал", url="https://t.me/+m3ecTPqE9owyZjUy")
    buy_privat = InlineKeyboardButton(text = "🛒 Купить приват", url="tg://resolve?domain=playgirl_admin")
    start = InlineKeyboardMarkup(inline_keyboard = [[send_photo, links],
                                                    [buy_privat]])
    return start
