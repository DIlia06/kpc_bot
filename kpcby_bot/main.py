import asyncio
from aiogram import Bot, Dispatcher


TOKEN = '8337047101:AAEMepjuRafztG8HOhDPFlH6EJL14wY-8J8'

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    register_routes(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stop')