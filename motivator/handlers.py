import random
from telebot import TeleBot
from quotes import motivations

# Декоратор для отримання ID користувача
def get_id(func):
    def wrapper(message, *args, **kwargs):
        user_id = message.from_user.id  # Отримуємо ID користувача
        print(f"ID користувача: {user_id}")  # Логування ID
        return func(message, user_id, *args, **kwargs)  # Передаємо ID далі
    return wrapper

def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    @get_id  # Використовуємо кастомний декоратор
    def send_welcome(message, user_id):
        bot.reply_to(message, f"Привіт! Твій ID: {user_id}. Напиши мені /quote, і я поділюся з тобою мотиваційною цитатою!")

    @bot.message_handler(commands=['quote'])
    @get_id  # Використовуємо кастомний декоратор
    def send_quote(message, user_id):
        random_quote = random.choice(motivations)
        bot.reply_to(message, f"Ось твоя мотиваційна цитата, користувач {user_id}:\n\n{random_quote}")

    @bot.message_handler(func=lambda message: True)  # Обробник для всіх інших повідомлень
    @get_id  # Використовуємо кастомний декоратор
    def send_message(message, user_id):
        bot.reply_to(message, f"Твій ID: {user_id}. Напиши /quote, щоб отримати мотиваційну цитату. 💡")


