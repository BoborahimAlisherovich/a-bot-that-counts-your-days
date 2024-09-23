
import datetime
from aiogram.types import Message
from loader import dp


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
