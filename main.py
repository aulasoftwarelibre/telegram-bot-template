#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hackathon import bot
import json
import logging
import os
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
            bot.process_new_updates([telebot.types.Update.de_json(self.request.body['message'].decode('utf-8'))])
        except Exception as e:
            logging.error(repr(e))


bot.remove_webhook()

if bot.threaded:
    logging.info('Polling...')
    bot.polling()
    exit(0)

heroku_url = os.environ.get('HEROKU_URL', False)
if not heroku_url:
    raise Exception('No se ha definido HEROKU_URL')

logging.info('Listening...')
bot.set_webhook(url="%s/webhook" % heroku_url.rstrip('/'))
app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/webhook', WebhookHandler)
], debug=True)
