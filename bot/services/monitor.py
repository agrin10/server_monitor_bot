import asyncio
from bot.utils.system import get_cpu, get_ram
from bot.config import Config

last_cpu_alert = False
last_ram_alert = False

async def monitor_system(bot):
    global last_cpu_alert , last_ram_alert
    while True:
        cpu = get_cpu()
        ram = get_ram()

        #cpu alert 
        if cpu >=Config.CPU_ALERT and not last_cpu_alert:
            await bot.send_message(
                Config.ADMIN_ID,
                f"🚨 CPU ALERT\n\nCPU usage is {cpu}%"
            )
            last_cpu_alert = True

        if cpu < Config.CPU_ALERT:
            last_cpu_alert = False

        # ram alert
        if ram >= Config.MEMORY_ALERT and not last_ram_alert:
            await bot.send_message(
                Config.ADMIN_ID,
                f"🚨 MEMORY ALERT\n\nMemory usage is {ram}%"
            )
            last_ram_alert = True
        if ram < Config.MEMORY_ALERT:
            last_ram_alert = False