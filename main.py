import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
import logging
from bot.config import Config

from bot.handlers import start, status , set_threshold
from bot.services.monitor import monitor_system

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def main():
    session = AiohttpSession(proxy=Config.PROXY_URL)
    bot = Bot(
        token=Config.BOT_TOKEN,
        session=session
    )

    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(status.router)
    dp.include_router(set_threshold.router)

    # Start background monitoring task
    asyncio.create_task(monitor_system(bot))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
