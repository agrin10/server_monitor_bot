import psutil
import time 

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_ram():
    ram = psutil.virtual_memory()
    return ram.percent

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime = current_time - boot_time
    return int(uptime)
