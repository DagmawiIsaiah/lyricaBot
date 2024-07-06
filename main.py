import os

from dotenv import load_dotenv
import telebot

import scrap

load_dotenv()

API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(content_types=['text'])
def send_lyrics(message):
    lyrics = scrap.Scrap(message.text).get_deposits()
    bot.send_message(message.chat.id, f"{message.text} \n {lyrics}")

bot.polling()
