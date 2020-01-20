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


def index(request):
    bot.remove_webhook()
    bot.set_webhook(url="https://www.baraeja.com/{}".format('scrape'))
    return HttpResponse('webhook setted')


def scrape(request):
    if request.method == 'POST':
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return HttpResponse('success')