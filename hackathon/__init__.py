import os

from telebot import TeleBot
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get('BOT_TOKEN')
if not token:
    raise Exception('No se ha definido BOT_TOKEN')


bot = TeleBot(token, os.environ.get('POLLING', False))

import command
