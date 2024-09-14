import config
import telebot
from config import token
import random
from random import choice



bot = telebot.TeleBot(token)


@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hi there, I am Shtenkes_bot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
""")

@bot.message_handler(commands=['info','help'])
def send_welcome(message):
    bot.reply_to(message, """
        Theres my commands:
/start
or you can send any message and see what i do
                            """)
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'hello' or message.text == 'hi':
        bot.reply_to(message, f'hello {message.from_user.username}')
    else: 
        bot.reply_to(message, message.text)


bot.infinity_polling()
