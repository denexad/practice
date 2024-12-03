from dotenv import load_dotenv 
import os

def setup_utils():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    if not token:
        raise ValueError("Токен не знайдено в .env файлі.")
    return token

