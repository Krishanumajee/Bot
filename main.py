import requests
from telegram.ext import Updater, MessageHandler, Filters
import datetime
import pytz
import os

# Telegram Bot Token
my_secret = os.environ[-1001961606497]


# Function to handle incoming messages
def handle_message(update, context):
  text = update.message.text

  # Check if the message matches the specified format "#<xyz>"
  if text.startswith("#") and len(text[1:]) == 10 and text[1:].isdigit():
    xyz = text[1:]  # Extracting <xyz> from the message
    api_url = f"https://freefireapi.com.br/api/like_id?region=ind&id={xyz}"

    try:
      # Sending a GET request to the API
      response = requests.get(api_url)
      api_response = response.json()

      # Extracting required data from the API response
      uid = xyz
      name = api_response['basicInfo']['nickname']
      level = api_response['basicInfo']['level']
      likes = api_response['basicInfo']['liked']
      last_login_unix = int(api_response['basicInfo']['lastLoginAt'])
      xp = api_response['basicInfo']['exp']
      br_points = api_response['basicInfo']['rankingPoints']
      bpl = api_response['basicInfo']['badgeCnt']
      cs_points = api_response['basicInfo']['csRankingPoints']
      cs_rank = "LoL"
      # Converting last login time to Indian Standard Time (IST)
      ist = pytz.timezone('Asia/Kolkata')
      last_login_utc = datetime.datetime.utcfromtimestamp(last_login_unix)
      last_login_ist = last_login_utc.replace(tzinfo=pytz.utc).astimezone(ist)
      last_login = last_login_ist.strftime('%d %B %Y %I:%M %p')

      # Convert createAt Unix timestamp to Indian Standard Time (IST)
      created_at_unix = int(api_response['basicInfo']['createAt'])
      created_at_utc = datetime.datetime.utcfromtimestamp(created_at_unix)
      created_at_ist = created_at_utc.replace(tzinfo=pytz.utc).astimezone(ist)
      created_at = created_at_ist.strftime('%d %B %Y %I:%M %p')

      # Determine BR Rank based on rankingPoints
      if 1000 <= br_points <= 1100:
        br = "Bronze 1"
      elif 1100 < br_points <= 1200:
        br = "Bronze 2"
      elif 1200 < br_points <= 1300:
        br = "Bronze 3"
      elif 1300 < br_points <= 1400:
        br = "Silver 1"
      elif 1400 < br_points <= 1500:
        br = "Silver 2"
      elif 1500 < br_points <= 1600:
        br = "Silver 3"
      elif 1600 < br_points <= 1725:
        br = "Gold 1"
      elif 1725 < br_points <= 1850:
        br = "Gold 2"
      elif 1850 < br_points <= 1975:
        br = "Gold 3"
      elif 1975 < br_points <= 2100:
        br = "Platinum 1"
      elif 2100 < br_points <= 2350:
        br = "Platinum 2"
      elif 2350 < br_points <= 2475:
        br = "Platinum 3"
      elif 2475 < br_points <= 2600:
        br = "Platinum 4"
      elif 2600 < br_points <= 2750:
        br = "Diamond 1"
      elif 2750 < br_points <= 2900:
        br = "Diamond 2"
      elif 2900 < br_points <= 3050:
        br = "Diamond 3"
      elif 3050 < br_points <= 3200:
        br = "Diamond 4"
      else:
        br = "Heroic"

      if cs_points == 1:
        cs_rank = "Bronze 1 (1 Star)"
      elif cs_points == 2:
        cs_rank = "Bronze 1 (2 Star)"
      elif cs_points == 3:
        cs_rank = "Bronze 1 (3 Star)"
      elif cs_points == 4:
        cs_rank = "Bronze 2 (1 Star)"
      elif cs_points == 5:
        cs_rank = "Bronze 2 (2 Star)"
      elif cs_points == 6:
        cs_rank = "Bronze 2 (3 Star)"
      elif cs_points == 7:
        cs_rank = "Bronze 3 (1 Star)"
      elif cs_points == 8:
        cs_rank = "Bronze 3 (2 Star)"
      elif cs_points == 9:
        cs_rank = "Bronze 3 (3 Star)"
      elif cs_points == 10:
        cs_rank = "Silver 1 (1 Star)"
      elif cs_points == 11:
        cs_rank = "Silver 1 (2 Star)"
      elif cs_points == 12:
        cs_rank = "Silver 1 (3 Star)"
      elif cs_points == 13:
        cs_rank = "Silver 1 (4 Star)"
      elif cs_points == 14:
        cs_rank = "Silver 2 (1 Star)"
      elif cs_points == 15:
        cs_rank = "Silver 2 (2 Star)"
      elif cs_points == 16:
        cs_rank = "Silver 2 (3 Star)"
      elif cs_points == 17:
        cs_rank = "Silver 2 (4 Star)"
      elif cs_points == 18:
        cs_rank = "Silver 3 (1 Star)"
      elif cs_points == 19:
        cs_rank = "Silver 3 (2 Star)"
      elif cs_points == 20:
        cs_rank = "Silver 3 (3 Star)"
      elif cs_points == 21:
        cs_rank = "Silver 3 (4 Star)"
      elif cs_points == 22:
        cs_rank = "Gold 1 (1 Star)"
      elif cs_points == 23:
        cs_rank = "Gold 1 (2 Star)"
      elif cs_points == 24:
        cs_rank = "Gold 1 (3 Star)"
      elif cs_points == 25:
        cs_rank = "Gold 1 (4 Star)"
      elif cs_points == 26:
        cs_rank = "Gold 2 (1 Star)"
      elif cs_points == 27:
        cs_rank = "Gold 2 (2 Star)"
      elif cs_points == 28:
        cs_rank = "Gold 2 (3 Star)"
      elif cs_points == 29:
        cs_rank = "Gold 2 (4 Star)"
      elif cs_points == 30:
        cs_rank = "Gold 3 (1 Star)"
      elif cs_points == 31:
        cs_rank = "Gold 3 (2 Star)"
      elif cs_points == 32:
        cs_rank = "Gold 3 (3 Star)"
      elif cs_points == 33:
        cs_rank = "Gold 3 (4 Star)"
      elif cs_points == 34:
        cs_rank = "Gold 4 (1 Star)"
      elif cs_points == 35:
        cs_rank = "Gold 4 (2 Star)"
      elif cs_points == 36:
        cs_rank = "Gold 4 (3 Star)"
      elif cs_points == 37:
        cs_rank = "Gold 4 (4 Star)"
      elif cs_points == 38:
        cs_rank = "Platinum 1 (1 Star)"
      elif cs_points == 39:
        cs_rank = "Platinum 1 (2 Star)"
      elif cs_points == 40:
        cs_rank = "Platinum 1 (3 Star)"
      elif cs_points == 41:
        cs_rank = "Platinum 1 (4 Star)"
      elif cs_points == 42:
        cs_rank = "Platinum 1 (5 Star)"
      elif cs_points == 43:
        cs_rank = "Platinum 2 (1 Star)"
      elif cs_points == 44:
        cs_rank = "Platinum 2 (2 Star)"
      elif cs_points == 45:
        cs_rank = "Platinum 2 (3 Star)"
      elif cs_points == 46:
        cs_rank = "Platinum 2 (4 Star)"
      elif cs_points == 47:
        cs_rank = "Platinum 2 (5 Star)"
      elif cs_points == 48:
        cs_rank = "Platinum 3 (1 Star)"
      elif cs_points == 49:
        cs_rank = "Platinum 3 (2 Star)"
      elif cs_points == 50:
        cs_rank = "Platinum 3 (3 Star)"
      elif cs_points == 51:
        cs_rank = "Platinum 3 (4 Star)"
      elif cs_points == 52:
        cs_rank = "Platinum 3 (5 Star)"
      elif cs_points == 52:
        cs_rank = "Platinum 4 (1 Star)"
      elif cs_points == 53:
        cs_rank = "Platinum 4 (2 Star)"
      elif cs_points == 54:
        cs_rank = "Platinum 4 (3 Star)"
      elif cs_points == 55:
        cs_rank = "Platinum 4 (4 Star)"
      elif cs_points == 56:
        cs_rank = "Diamond 1 (1 Star)"
      elif cs_points == 57:
        cs_rank = "Diamond 1 (2 Star)"
      elif cs_points == 58:
        cs_rank = "Diamond 1 (3 Star)"
      elif cs_points == 59:
        cs_rank = "Diamond 1 (4 Star)"
      elif cs_points == 60:
        cs_rank = "Diamond 1 (1 Star)"
      elif cs_points == 61:
        cs_rank = "Diamond 1 (2 Star)"
      elif cs_points == 62:
        cs_rank = "Diamond 1 (3 Star)"
      elif cs_points == 63:
        cs_rank = "Diamond 1 (4 Star)"
      elif cs_points == 64:
        cs_rank = "Diamond 1 (5 Star)"
      elif cs_points == 65:
        cs_rank = "Diamond 2 (1 Star)"
      elif cs_points == 66:
        cs_rank = "Diamond 2 (2 Star)"
      elif cs_points == 66:
        cs_rank = "Diamond 2 (3 Star)"
      elif cs_points == 67:
        cs_rank = "Diamond 2 (4 Star)"
      elif cs_points == 68:
        cs_rank = "Diamond 2 (5 Star)"
      elif cs_points == 69:
        cs_rank = "Diamond 3 (1 Star)"
      elif cs_points == 70:
        cs_rank = "Diamond 3 (2 Star)"
      elif cs_points == 71:
        cs_rank = "Diamond 3 (3 Star)"
      elif cs_points == 72:
        cs_rank = "Diamond 3 (4 Star)"
      elif cs_points == 73:
        cs_rank = "Diamond 3 (5 Star)"
      elif cs_points == 74:
        cs_rank = "Diamond 4 (1 Star)"
      elif cs_points == 75:
        cs_rank = "Diamond 4 (2 Star)"
      elif cs_points == 76:
        cs_rank = "Diamond 4 (3 Star)"
      elif cs_points == 77:
        cs_rank = "Diamond 4 (4 Star)"
      elif cs_points >= 78 and cs_points <= 128:
        h_rank = cs_points - 77
        cs_rank = "Heroic " + str(h_rank) + " Star"
      elif cs_points >= 128:
        m_rank = cs_points - 128
        cs_rank = "Master " + str(m_rank) + " Star"

      # ... (rest of the conditions for determining BR Rank)

      # Constructing the message
      message = (f"UID: {uid}\n"
                 f"Name: {name}\n"
                 f"Level: {level}\n"
                 f"Likes: {likes}\n"
                 f"Exp: {xp}\n"
                 f"BR Rank: {br}\n"
                 f"CS Rank: {cs_rank}")
                 f"Booyah Pass Level: {bpl}\n"
                 f"Created On: {created_at}\n"
                 f"Last Login: {last_login}\n"
                 f"Join Main Channel [smartclown_ofc](https://t.me/smartclown_ofc)\n"

      # Sending the formatted message as a reply to the user
      context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    except Exception as e:
      print(f"An error occurred: {e}")


# Set up the bot and start polling for messages
def main():
  updater = Updater(token=my_secret, use_context=True)
  dp = updater.dispatcher
  dp.add_handler(
      MessageHandler(Filters.text & ~Filters.command, handle_message))
  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
  main()
