import logging
import os
import sys
from hackathon import bot

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info('Setting webhook...')


def set_webhook():
    '''
    Configura el webhook del hackathon. Puede ejecutarse en local si se configura HEROKU_URL en el .env
    En remoto ejecutar heroku ...
    '''
    heroku_url = os.environ.get('HEROKU_URL', False)
    if not heroku_url:
        raise Exception('No se ha definido HEROKU_URL')

    response = bot.set_webhook(url="%s/webhook" % heroku_url.rstrip('/'))
    logging.info(response)


if __name__ == "__main__":
    set_webhook()
