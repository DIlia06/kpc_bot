import logging
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

from kpcby_bot.settings import API_TOKEN, API_BASE_URL


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
router = Router()
dp = Dispatcher()

@router.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Как я могу помочь? У тебя есть вопросы о нас или ты хочешь оставить обращение.")

@router.message(F.text.lower() in ['какой ваш адрес?', 'где вы находитесь?', 'где вы?'])
async def address_query(message: types.Message):
    response = {
        "response": "Мы находимся по адресу: город Минск, улица Олешева 3, офис 323"
    }
    await message.answer(response["response"])

@router.message()
async def handle_message(message: types.Message):
    appeal_data = {
        "user_name": message.from_user.full_name,
        "message": message.text
    }
    response = requests.post(f"{API_BASE_URL}appeal", json=appeal_data)

    if response.status_code == 201:
        await message.answer("Ваше сообщение успешно отправлено!")
    else:
        await message.answer("Произошла ошибка при отправке сообщения.")

if __name__ == '__main__':
    try:
        asyncio.run(bot)
    except KeyboardInterrupt:
        print('Bot stop')