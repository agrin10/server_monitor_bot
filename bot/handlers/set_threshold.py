from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.settings import Settings
from bot.config import Config
from bot.database.settings_repo import update_cpu, update_ram


router = Router()   

@router.message(Command("set_threshold"))
async def set_threshold_handler(message: Message):
    """Handle the /set_threshold command to set CPU and memory thresholds."""
    if message.from_user.id != Config.ADMIN_ID:
        await message.answer("❌ You are not authorized to use this command.")
        return
    parts = message.text.split()

    if len(parts) != 3:
        await message.answer(
            "❌ Invalid format.\n\n"
            "Use:\n"
            "/set_threshold cpu 80\n"
            "/set_threshold ram 75"
        )
        return

    _, target , value = parts
    target = target.lower() 

    if not value.isdigit():
        await message.answer("❌ Threshold value must be a number.")
        return
    
    value = float(value)
    if not 1 <=value <= 100:
        await message.answer("❌ Threshold value must be between 1 and 100.")
        return
    
    if target == "cpu":
        Settings.cpu_threshold = value
        Settings.reset_cpu_alert()
        update_cpu(value)
        await message.answer(f"✅ CPU threshold set to {value}%")

    elif target in ("ram", "memory"):
        Settings.ram_threshold = value
        Settings.reset_ram_alert()
        update_ram(value)
        await message.answer(f"✅ Memory threshold set to {value}%")

    else:
        await message.answer("❌ Invalid target. Use 'cpu' or 'ram'.")
