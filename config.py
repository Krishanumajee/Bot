import telebot
import os
TOKEN = os.getenv('TELEGRAM_BOT_API_ID')
bot = telebot.TeleBot(Token)