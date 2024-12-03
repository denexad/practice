from telebot import TeleBot
from utils import setup_utils
from handlers import register_handlers

def main():
    token = setup_utils()  # Забули викликати функцію (дужки відсутні)
    bot = TeleBot(token)

    register_handlers(bot)

    print("Бот запущений...")
    bot.polling()

if __name__ == "__main__":
    main()
