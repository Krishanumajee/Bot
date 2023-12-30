import telebot
import datetime
import requests
from telebot import types



target_group_chat_id = -1001989654002

def jishsuxb(nssisj):
    dt_object = datetime.datetime.utcfromtimestamp(nssisj)
    formatted_date_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date_time





def get_data_jinxx(url):
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(e)
    if 'basicInfo' in data:
        nickname = data['basicInfo']['nickname']
        level = data['basicInfo']['level']
        bannerId = data['basicInfo']['bannerId']
        headPic = data['basicInfo']['headPic']
        rankingPoints = data['basicInfo']['rankingPoints']
        csRankingPoints = data['basicInfo']['csRankingPoints']
        lastLoginAt = jishsuxb(int(data['basicInfo']['lastLoginAt']))
        createAt = jishsuxb(int(data['basicInfo']['createAt']))
        liked = int(data['basicInfo']['liked'])
        accountId = int(data['basicInfo']['accountId'])
        message_text_jinxx = f"""
🤖 Dᴇᴀʀ `{nickname}`, Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ Dᴇᴛᴀɪʟs Aʀᴇ Hᴇʀᴇ 👇
👍 Lɪᴋᴇs: `{liked}`
📈 Lᴠ::{level}
⭐ Bʀ Sᴄᴏʀᴇ: {rankingPoints}
⭐ Cs Sᴄᴏʀᴇ: {csRankingPoints}
⌛ Lᴀsᴛ Lᴏɢɪɴ: {lastLoginAt}
⌛ Aᴄᴄᴏᴜɴᴛ Cʀᴇᴀᴛᴇᴅ: {createAt}
"""
        return data, message_text_jinxx, nickname, level, headPic, liked, accountId
    else:
        data = "error"
        message_text_jinxx = ""
        return data, message_text_jinxx
    
    
    
