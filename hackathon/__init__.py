import os

from telebot import TeleBot
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get('BOT_TOKEN')
if not token:
    raise Exception('No se ha definido BOT_TOKEN')

secret_token = os.environ.get('SECRET_TOKEN', False)
if not secret_token:
    raise Exception('No se ha definido SECRET_TOKEN')

app_name = os.environ.get('HEROKU_APP_NAME', False)
if not app_name:
    raise Exception('No se ha definido HEROKU_APP_NAME')


bot = TeleBot(token, os.environ.get('POLLING', False))

import command
