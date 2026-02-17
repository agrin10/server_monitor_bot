import asyncio
from bot.utils.system import get_cpu, get_ram
from bot.config import Config
from bot.database.redis_client import redis_client
from bot.database.settings_repo import get_cpu as get_cpu_threshold
from bot.database.settings_repo import get_ram as get_ram_threshold


CPU_ALERT_KEY = "alert:cpu"
RAM_ALERT_KEY = "alert:ram"


async def monitor_system(bot):
    while True:
        cpu = get_cpu()
        ram = get_ram()

        cpu_threshold = get_cpu_threshold()
        ram_threshold = get_ram_threshold()

        # ------------------ CPU ------------------
        if cpu >= cpu_threshold:

            # Check if cooldown key exists
            if not redis_client.exists(CPU_ALERT_KEY):

                await bot.send_message(
                    Config.ADMIN_ID,
                    f"🚨 CPU ALERT\nCPU: {cpu}%\nThreshold: {cpu_threshold}%"
                )

                # Set cooldown (60 sec or your CHECK_INTERVAL)
                redis_client.set(CPU_ALERT_KEY, 1, ex=60)

        else:
            # Reset alert immediately if usage goes back down
            redis_client.delete(CPU_ALERT_KEY)

        # ------------------ RAM ------------------
        if ram >= ram_threshold:

            if not redis_client.exists(RAM_ALERT_KEY):

                await bot.send_message(
                    Config.ADMIN_ID,
                    f"🚨 RAM ALERT\nRAM: {ram}%\nThreshold: {ram_threshold}%"
                )

                redis_client.set(RAM_ALERT_KEY, 1, ex=60)

        else:
            redis_client.delete(RAM_ALERT_KEY)

        await asyncio.sleep(Config.CHECK_INTERVAL)
