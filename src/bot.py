import telebot
import config
from _mongodb import MongoDB
from wildberries_parser import Parser

bot = telebot.TeleBot(config.TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['get_brand'])
def get_brand(message):
    article = message.text.split()[1]
    data = Parser.parse_article(article)['data']['products'][0]
    # MongoDB.insert_data(data)
    bot.reply_to(message, data['brand'])


@bot.message_handler(commands=['get_title'])
def get_title(message):
    article = message.text.split()[1]
    data = Parser.parse_article(article)['data']['products'][0]
    # MongoDB.insert_data(data)
    bot.reply_to(message, data['name'])


bot.infinity_polling()
