from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from telebot import TeleBot, types
import os


TOKEN = os.environ['TOKEN']
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Welcome")


def scrape(request):
    json_str = request.body.decode('UTF-8')
    update = types.Update.de_json(json_str)
    bot.process_new_updates([update])

    return HttpResponse('success')