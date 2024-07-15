import os

from dotenv import load_dotenv
import telebot
import azapi

load_dotenv()

API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)
API = azapi.AZlyrics('google', accuracy=0.5)

# Load environment variables from .env file
load_dotenv()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello, I'm a bot that can send you lyrics of any song you want. Just type the name of the artist and the name of the song, separated by a comma. For example: Adele, Hello \n developer: https://t.me/lyrics_gen_bot/lyrica")

@bot.message_handler(content_types=['text'])
def send_lyrics(message):
    message_text = message.text.split(', ')
    API.artist = message_text[0]
    API.title = message_text[1]
    API.getLyrics()
    lyrics = API.lyrics
    
    if len(lyrics) < 30:
        bot.send_message(
        message.chat.id,
        "Hello, I'm a bot that can send you lyrics of any song you want. Just type the name of the artist and the name of the song, separated by a comma.\n\n"
        "**For example:** Adele, Hello\n\n"
        "**Developer:** [lyrics_gen_bot/lyrica](https://t.me/lyrics_gen_bot/lyrica)",
        parse_mode='Markdown'
        )
        return

    else:
        # Construct the message with bold formatting
        bold_artist_title = f"*{message_text[0].title()} - {message_text[1].title()}*"
        full_message = f"{bold_artist_title}\n\n{lyrics}"

        # Send the message with Markdown style for bold
        bot.send_message(message.chat.id, full_message, parse_mode='Markdown')

try:
    bot.polling()
except Exception as e:
    print(e)
    bot.stop_polling()
    bot.polling()