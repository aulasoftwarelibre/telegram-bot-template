import logging
import sys
from hackathon import bot, secret_token, app_name

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def set_webhook(force=False):
    """
    Configura el webhook del bot.
    """
    webhook = bot.get_webhook_info()
    if webhook.url and not force:
        logging.info("Webhook already setup")
        return

    logging.info('Setting webhook...')
    response = bot.set_webhook(url="https://%s.herokuapp.com/webhook%s" % (app_name.strip(), secret_token.strip()))
    logging.info(response)


if __name__ == "__main__":
    set_webhook(True)
