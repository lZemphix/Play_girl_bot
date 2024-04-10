from keyboards import inline
from data import desc
from utils import states
from data.config import *
from aiogram.utils.media_group import MediaGroupBuilder

print("bot was started")
media_group_cache = {}

async def send_photo_action(message, state, bot):
    if message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
        await message.answer("Фото отправлено на модерацию, ожидайте.")
        await bot.send_photo(chat_id=6503681467, photo=message.photo[-1].file_id)
        await state.clear()
    else:
        await message.answer("Что-то пошло не так. Возможно вы пытаетесь отправить фото как файл. Отправье фото как изображение или введите /cancel для отмены")

async def send_photo_action(message, state, bot):
    if message.media_group_id:
        if message.media_group_id not in media_group_cache:
            media_group_cache[message.media_group_id] = MediaGroupBuilder()
        media_group_cache[message.media_group_id].add_photo(type = "photo", media = message.photo[-1].file_id)
        await message.answer("Фото отправлено на модерацию, ожидайте.")
        await send_media_group(bot, message.media_group_id, state)
        await state.clear()
    elif message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
        await message.answer("Фото отправлено на модерацию, ожидайте.")
        await bot.send_photo(chat_id=6503681467, photo=message.photo[-1].file_id)
        await state.clear()
    else:
        await message.answer("Ошибка. Возможно вы пытаетесь отправить фото как файл. Отправье фото как изображение или введите /cancel для отмены")

async def send_media_group(bot, media_group_id, state):
    try:
        await bot.send_media_group(chat_id=6503681467, media=media_group_cache[media_group_id].build())
        del media_group_cache[media_group_id]
        await state.clear()
    except KeyError:
        await state.clear()
        return

async def send_photo_start_action(callback, state):
    await callback.message.answer("Отправьте одно или несколько фотографий. Введите /cancel для отмены")
    await state.set_state(states.send_photo.photography)

async def buy_privat_action(callback, state):
    await callback.message.answer(desc.top_up, reply_markup=inline.rules_kb())
    await state.set_state(states.top_up.rules)


















        
 