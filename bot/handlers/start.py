from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.config import Config

router = Router()

@router.message(CommandStart())
async def start_command_handler(message: Message):
    if message.from_user.id != Config.ADMIN_ID:
        await message.answer("You are not authorized to use this bot.")
        return
    
    await message.answer(
        "🖥 Server Monitoring Bot\n\n"
        "Commands:\n"
        "/status – Server status"
    )

