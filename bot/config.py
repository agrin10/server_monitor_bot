import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))  
    PROXY_URL = os.getenv("PROXY_URL") 
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
    CPU_ALERT = int(os.getenv("CPU_ALERT_THRESHOLD", 80))
    MEMORY_ALERT = int(os.getenv("MEMORY_ALERT_THRESHOLD", 80))
    
class TestConfig:
    BOT_TOKEN   = "TEST_BOT_TOKEN"
    ADMIN_ID    = "123456789 "

class ProdConfig:
    BOT_TOKEN   = os.getenv("BOT_TOKEN")
    ADMIN_ID    = int(os.getenv("ADMIN_ID"))    