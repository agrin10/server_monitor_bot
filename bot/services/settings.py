from bot.config import Config

class Settings:
    cpu_threshold: float = Config.CPU_ALERT
    memory_threshold: float = Config.MEMORY_ALERT

    cpu_alert_active: bool = False
    ram_alert_active: bool = False

    @classmethod
    def reset_cpu_alert(cls):
        cls.cpu_alert_active = False

    @classmethod
    def reset_ram_alert(cls):
        cls.ram_alert_active = False
