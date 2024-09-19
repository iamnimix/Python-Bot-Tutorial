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


@bot.message_handler(content_types=['document', 'audio'])
def check_doc_audio(message):
    if message.content_type == 'document':
        bot.reply_to(message, "it's a document")
    elif message.content_type == 'audio':
        bot.reply_to(message, "it's an audio")


@bot.message_handler(regexp=r'^Hello$')
def say_hello(message):
    bot.reply_to(message, 'Hello :)')


@bot.message_handler(func=lambda message: message.content_type == 'text')
def handle_text(message):
    bot.send_message(message.chat.id, message.chat.username)


bot.infinity_polling()
