import telebot
import os
import re
from telebot import types
from jinxx.handler import *
from config import bot


@bot.message_handler(func=lambda message: True)
def new_mes(message):
    try:
        UserID = message.text[1:]
        #if message.chat.id = target_group_chat_id and '#' in message.text and re.match("^[0-9]{9,11}$", UserID):
        if '#' in message.text and re.match("^[0-9]{9,11}$", UserID):
            url = f"https://freefireapi.com.br/api/like_id?id={UserID}&region=ind"
            data, message_text_jinxx, nickname, level, headPic, liked, accountId = get_data_jinxx(url)
            if "error" not in data:
                webappurl = f"https://jinxx6-6.github.io/Sjsu7w?uid={accountId}&name={nickname}&lvl={level}&like={liked}&headPic={headPic}"
                bot.reply_to(message, message_text_jinxx, parse_mode="Markdown")
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=save.message_id)
    except Exception as e:
        print(e)
          
if __name__ == '__main__':
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(e)
