import logging
import os
import sys
from hackathon import bot

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info('Setting webhook...')


def set_webhook():
    '''
    Configura el webhook del hackathon. Puede ejecutarse en local si se configura HEROKU_APP_NAME en el .env
    '''
    app_name = os.environ.get('HEROKU_APP_NAME', False)
    if not app_name:
        raise Exception('No se ha definido HEROKU_APP_NAME')

    response = bot.set_webhook(url="https://%s.herokuapp.com/webhook" % app_name.strip())
    logging.info(response)


if __name__ == "__main__":
    set_webhook()
