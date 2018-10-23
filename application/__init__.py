# coding=utf-8

import os

from flask import Flask
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')
if not TOKEN:
    raise Exception('No se ha definido BOT_TOKEN')

SECRET_TOKEN = os.environ.get('SECRET_TOKEN', False)
if not SECRET_TOKEN:
    raise Exception('No se ha definido SECRET_TOKEN')

HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', False)
if not HEROKU_APP_NAME:
    raise Exception('No se ha definido HEROKU_APP_NAME')

DATABASE_URL = os.environ.get('DATABASE_URL', False)
if not DATABASE_URL:
    raise Exception('No se ha definido DATABASE_URL')

bot = TeleBot(TOKEN, os.environ.get('POLLING', False))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add more files here
from application import db
from application import commands
