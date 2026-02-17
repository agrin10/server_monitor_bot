from bot.database.settings_repo import (
    get_cpu,
    get_ram,
    update_cpu,
    update_ram,
    reset_cpu_alert,
    reset_ram_alert
)

class Settings:
    @property
    def cpu_threshold(self):
        return get_cpu()
    
    @property
    def ram_threshold(self):
        return get_ram()
    
    @staticmethod
    def reset_cpu_alert():
        reset_cpu_alert()

    @staticmethod
    def reset_ram_alert():
        reset_ram_alert()

    

settings = Settings()
