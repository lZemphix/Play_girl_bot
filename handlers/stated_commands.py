from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from handlers.actions import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from utils import states

router = Router()

@router.message(Command("start"), StateFilter(default_state))
async def start(message: Message):
    await message.answer(f"""Привет, {message.from_user.first_name}! Выбери действие:""", reply_markup=inline.start_kb())

@router.message(Command("cancel"), ~StateFilter(default_state))
async def cancel_accept(message: Message, state: FSMContext):
    await message.answer("Вы отменили действие!")
    await state.clear()
    await message.answer(f"""Привет, {message.from_user.first_name}! Выбери действие:""", reply_markup=inline.start_kb())

@router.message(Command("cancel"))
async def incorrect_cancel(message: Message, state: FSMContext):
    await message.answer("Отменять нечего!")

@router.callback_query(F.data.in_('send_photo'), StateFilter(default_state))
async def send_photo_start(callback: CallbackQuery, state: FSMContext):
    await send_photo_start_action(callback, state)


@router.message(StateFilter(states.send_photo.photography))
async def send_photo(message: Message, state: FSMContext, bot: Bot):
    await send_photo_action(message, state, bot)
