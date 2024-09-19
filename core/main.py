import telebot
import json
import os
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # bot.reply_to(message, 'Hello!!!')
    bot.send_message(message.chat.id, json.dumps(message.chat.__dict__, indent=1, ensure_ascii=False))


bot.infinity_polling()
