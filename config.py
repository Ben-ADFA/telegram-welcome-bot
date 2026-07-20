import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing from .env")

if not CHAT_ID:
    raise ValueError("CHAT_ID is missing from .env")

CHAT_ID = int(CHAT_ID)