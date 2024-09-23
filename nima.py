import datetime
from aiogram.types import Message

import speech_recognition as sr
from pydub import AudioSegment
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

API_TOKEN = '7227515766:AAFIfZ2fSbSLVgZX3NbmkYkoTE773Iw1odg'

# Bot va dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Foydalanuvchi tug'ilgan yil, oy va kunni kiritishi uchun start komandasini qo'llaymiz
@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Salom! Iltimos, tug'ilgan yilingizni, oyingizni va kuningizni YYYY-MM-DD formatida kiriting.")

# Foydalanuvchi tug'ilgan sanani kiritadi
@dp.message()
async def handle_date_input(message: Message):
    try:
        # Foydalanuvchi kiritgan sanani o'qiymiz
        birth_date = datetime.datetime.strptime(message.text, "%Y-%m-%d").date()
        
        # Hozirgi sanani aniqlaymiz
        current_date = datetime.date.today()

        # Tug'ilgan sanadan hozirgacha qancha kun o'tganini hisoblaymiz
        lived_days = (current_date - birth_date).days

        # Foydalanuvchiga yashagan kunlarini chiqaramiz
        await message.answer(f"Siz {lived_days} kun yashadingiz.")
    
    except ValueError:
        # Agar foydalanuvchi noto'g'ri formatda sana kiritgan bo'lsa
        await message.answer("Iltimos, tug'ilgan sanangizni to'g'ri formatda kiriting: YYYY-MM-DD.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
