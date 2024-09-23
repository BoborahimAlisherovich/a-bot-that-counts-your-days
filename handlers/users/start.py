from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Salom! Iltimos, tug'ilgan yilingizni, oyingizni va kuningizni YYYY-MM-DD formatida kiriting.")
    except:
        await message.answer(text="Salom! Iltimos, tug'ilgan yilingizni, oyingizni va kuningizni YYYY-MM-DD formatida kiriting.")
