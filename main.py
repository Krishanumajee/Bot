import telebot
import requests
import json
from datetime import datetime, timezone, timedelta
import calendar
import re
import os
TOKEN = os.getenv('TELEGRAM_BOT_API_ID')
bot = telebot.TeleBot(TOKEN)

target_group_chat_id = -1001961606497


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text
    if chat_id == target_group_chat_id:
    #if True:
        if '#' in text:
            hashtag = message.text[0]
            UserID = message.text[1:]
            if re.match("^[0-9]{9,11}$", UserID):
                print("UserID:", UserID)
    
                api_url = f'https://freefireapi.com.br/api/like_id?id={UserID}&region=IND'
                response = requests.get(api_url)
    
                try:
                    api_data = json.loads(response.text)
                    print(api_data)  
                    basic_info = api_data.get('basicInfo', {})
                    name = basic_info.get('nickname')
                    uid = basic_info.get('accountId')
                    level = basic_info.get('level')
                    likes = basic_info.get('liked')
                    Exp = basic_info.get('exp')
                    BRR = basic_info.get('rankingPoints')
                    CSR = basic_info.get('csRankingPoints')
                    create_at_timestamp = basic_info.get('createAt')
                    last_log = int(basic_info.get('lastLoginAt'))
                    
                    
                    if name is not None and uid is not None and level is not None and create_at_timestamp is not None:
                        
                        create_at_utc = (
                            datetime.utcfromtimestamp(int(create_at_timestamp)).replace(tzinfo=timezone.utc)
                            + timedelta(seconds=19800)  
                        )
                        create_at_utc2 = (
                            datetime.utcfromtimestamp(int(last_log)).replace(tzinfo=timezone.utc)
                            + timedelta(seconds=19800)  
                        )
                        formatted_date = datetime.utcfromtimestamp(last_log).strftime("%B %d, %Y at %I:%M:%S %p")
                        month_name = calendar.month_name[create_at_utc.month]
                        create_at_utc = create_at_utc.strftime(f'%B %d, %Y at %I:%M:%S %p')
                        reply_message = f"""*{name}* Your Account Was Created On {create_at_utc}
                        
UID: {uid}

Likes: {likes}

Level: {level}

Exp: {Exp}

BR Rank Point: {BRR}

CS Rank Point: {CSR}

You opened Free Fire last on {formatted_date}

Join Main Channel [smartclown_ofc](https://t.me/smartclown_ofc)
"""
                        bot.send_message(chat_id, reply_message, parse_mode="Markdown", disable_web_page_preview=True)
                    else:
                        print("Required fields are missing in the API response")
                
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON response: {e}")

bot.polling()
