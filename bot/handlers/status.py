from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.config import Config
from bot.utils.system import(
    get_cpu ,
    get_disk,
    get_ram,
    get_uptime
)

router = Router()

@router.message(Command("status"))
async def status_command_handler(message:Message):
    if message.from_user.id != Config.ADMIN_ID:
        await message.answer("You are not authorized to use this bot.")
        return
    
    cpu = get_cpu()
    mem = get_ram()
    disk = get_disk()
    uptime = get_uptime()

    text = (
        "📊 *Server Status*\n\n"
        f"🧠 CPU: {cpu}%\n"
        f"💾 RAM: {mem}%\n"
        f"📦 Disk: {disk}%\n"
        f"⏱ Uptime: {uptime}"
    )

    await message.answer(text, parse_mode="Markdown")
