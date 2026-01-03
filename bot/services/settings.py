from bot.database.settings_repo import get_settings

class Settings:
    cpu_threshold: int = 80
    ram_threshold: int = 80

    cpu_alert_active: bool = False
    ram_alert_active: bool = False

    @classmethod
    def load(cls):
        cpu, ram = get_settings()
        cls.cpu_threshold = cpu
        cls.ram_threshold = ram

    @classmethod
    def reset_cpu_alert(cls):
        cls.cpu_alert_active = False

    @classmethod
    def reset_ram_alert(cls):
        cls.ram_alert_active = False
