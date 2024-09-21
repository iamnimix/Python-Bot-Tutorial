import telebot
import json
import os
import logging
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


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
    logger.info('hello message!!!')
    bot.reply_to(message, 'Hello :)')


@bot.message_handler(commands=['setname'])
def set_name(message):
    bot.reply_to(message, 'What is your first name?')
    bot.register_next_step_handler(message, assign_first_name)


def assign_first_name(message):
    first_name = message.text
    bot.send_message(message.chat.id, 'What is your last name?')
    bot.register_next_step_handler(message, assign_last_name, first_name)


def assign_last_name(message, first_name):
    last_name = message.text
    bot.send_message(message.chat.id, f"Welcome {first_name} {last_name} to bot")


@bot.message_handler(func=lambda message: message.content_type == 'text')
def handle_text(message):
    bot.send_message(message.chat.id, message.chat.username)


bot.infinity_polling()
