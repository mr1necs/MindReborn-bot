import asyncio
from aiogram import Dispatcher, Bot
from app.config import BOT_TOKEN

from app.handlers import router
# from app.admin_handlers import router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")
