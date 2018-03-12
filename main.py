#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from hackathon import bot, secret_token
from webhook import set_webhook
import json
import logging
import os
import sys
import telebot
import traceback

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info('Starting...')

app = Flask(__name__)


@app.route('/me', methods=['GET'])
def send_me():
    """
    Devuelve información del bot
    """
    me = bot.get_me()
    return json.dumps(me, default=lambda o: o.__dict__, sort_keys=True, indent=4)


@app.route('/webhook'+secret_token, methods=['POST'])
def get_messages():
    """
    Se encarga de procesar los mensajes recibidos por el bot
    """
    try:
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    except Exception as e:
        logging.error("Se ha lanzado una excepcion")
        logging.error(repr(e))
        logging.error(traceback.format_exc())
    return "!", 200


if bot.threaded:
    logging.info('Polling...')
    bot.remove_webhook()
    bot.polling()
    exit(0)

if __name__ == '__main__':
    set_webhook()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
