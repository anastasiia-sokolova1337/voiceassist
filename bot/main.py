import telebot
from  config import  TOKEN
from  core import  *


bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, I'm a bot")
    
  

@bot.message_handler(commands=['shutdown'])
def shutdown(message):
    bot.send_message(message.chat.id, "Shutting down...")
    shutdown_pc()

#types 
#markup


bot.infinity_polling()

