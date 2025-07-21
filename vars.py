#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20031391"))
API_HASH = environ.get("API_HASH", "64a4dd9d4d4c7f7be23df45e61eb7869")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "8005640547"))
CREDIT = environ.get("CREDIT", "𝐑υ𝗍υ𝗋α𝗃 𝐆α𝗂𝗄ωαᑯ")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8005640547').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8005640547').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
