import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))  
    PROXY_URL = os.getenv("PROXY_URL") 
    
class TestConfig:
    BOT_TOKEN   = "TEST_BOT_TOKEN"
    ADMIN_ID    = "123456789 "

class ProdConfig:
    BOT_TOKEN   = os.getenv("BOT_TOKEN")
    ADMIN_ID    = int(os.getenv("ADMIN_ID"))    