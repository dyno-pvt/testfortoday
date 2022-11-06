import telebot

bot = telebot.TeleBot("5731095979:AAGSRrJ4lyeLtQ7ZouOFrGDB8IUlIDORxVw")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message , "hello")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message , "yes what do you need")

bot.infinity_polling()