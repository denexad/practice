import telebot
import time

TOKEN = "7902540030:AAGrv7d7PpDZr-QhPQqhgO9DPMEXP5znIxw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Я бот, який від 1000 віднімає 7. Напиши /subtract, щоб почати!"
    )

@bot.message_handler(commands=['subtract'])
def subtract(message):
    number = 1000
    chat_id = message.chat.id

    while number >= 0:
        bot.send_message(chat_id, str(number))
        number -= 7
        time.sleep(0.2)

    bot.send_message(chat_id, "Ви зійшли з розуму(")

if __name__ == "__main__":
    print("Бот запущений...")
    bot.infinity_polling()
