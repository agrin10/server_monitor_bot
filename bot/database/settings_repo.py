from bot.database.redis_client import redis_client

SETTINGS_KEY = "system:thresholds"


def update_cpu(value: float):
    redis_client.hset(SETTINGS_KEY, "cpu_threshold", value)


def update_ram(value: float):
    redis_client.hset(SETTINGS_KEY, "ram_threshold", value)


def get_cpu():
    value = redis_client.hget(SETTINGS_KEY, "cpu_threshold")
    return float(value) if value else 80.0


def get_ram():
    value = redis_client.hget(SETTINGS_KEY, "ram_threshold")
    return float(value) if value else 75.0


def reset_cpu_alert():
    redis_client.delete("alert:cpu")


def reset_ram_alert():
    redis_client.delete("alert:ram")
