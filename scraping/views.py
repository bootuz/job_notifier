from django.shortcuts import render

# Create your views here.
from telebot import TeleBot
import os


TOKEN = os.environ['TOKEN']
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome")
