import logging
import sys
from application import bot

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def get_webhook():
    """
    Lee el webhook del bot.
    """

    logging.info('Getting webhook...')
    response = bot.get_webhook_info()
    if not response.url:
        print "No hay url"
        return
    print ("URL: %s" % response.url)

    logging.info(response)

if __name__ == "__main__":
    get_webhook()
