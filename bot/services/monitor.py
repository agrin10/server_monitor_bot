import asyncio
from bot.utils.system import get_cpu, get_ram
from bot.config import Config
from bot.services.settings import Settings

async def monitor_system(bot):
    while True:
        cpu = get_cpu()
        ram = get_ram()

        # CPU
        if cpu >= Settings.cpu_threshold and not Settings.cpu_alert_active:
            await bot.send_message(
                Config.ADMIN_ID,
                f"🚨 CPU ALERT\nCPU: {cpu}%\nThreshold: {Settings.cpu_threshold}%"
            )
            Settings.cpu_alert_active = True

        if cpu < Settings.cpu_threshold:
            Settings.cpu_alert_active = False

        # RAM
        if ram >= Settings.memory_threshold and not Settings.ram_alert_active:
            await bot.send_message(
                Config.ADMIN_ID,
                f"🚨 RAM ALERT\nRAM: {ram}%\nThreshold: {Settings.memory_threshold}%"
            )
            Settings.ram_alert_active = True

        if ram < Settings.memory_threshold:
            Settings.ram_alert_active = False

        await asyncio.sleep(Config.CHECK_INTERVAL)
