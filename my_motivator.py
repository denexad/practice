import telebot
import random
from quotes import motivations

bot = telebot.TeleBot("7888421615:AAFkGFDBBPObTsSUeX_Y3XDEODLn5Gfi3HI")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я надихаючий бот. Напиши мені /quote, і я поділюся з тобою мотиваційною цитатою!")

@bot.message_handler(commands=['quote'])
def send_quote(message):
    random_quote = random.choice(motivations)
    bot.reply_to(message, random_quote)

@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.reply_to(message, "Напиши /quote, щоб отримати мотиваційну цитату. 💡")

bot.polling()