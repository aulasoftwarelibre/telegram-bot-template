#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hackathon import bot
from webhook import set_webhook
import json
import logging
import sys
import webapp2
import telebot


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info('Starting...')


class MeHandler(webapp2.RequestHandler):
    """
    Devuelve información del bot
    """
    def get(self):
        me = bot.get_me()
        self.response.write(json.dumps(me, default=lambda o: o.__dict__,
                                       sort_keys=True, indent=4))


class WebhookHandler(webapp2.RequestHandler):
    """
    Se encarga de procesar los mensajes recibidos por el bot
    """
    def post(self):
        try:
            bot.process_new_updates([telebot.types.Update.de_json(self.request.body['message'])])
        except Exception as e:
            logging.error("[2] Se ha lanzado una excepcion")
            logging.error(repr(e))


if bot.threaded:
    logging.info('Polling...')
    bot.remove_webhook()
    bot.polling()
    exit(0)

webhook = bot.get_webhook_info()
if not webhook.url:
    set_webhook()

logging.info('Listening...')
app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/webhook', WebhookHandler),
], debug=True)
