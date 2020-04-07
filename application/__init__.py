from application.config import TOKEN, SECRET_TOKEN, HEROKU_APP_NAME, DATABASE_URL
from application.config import bot, app, db
from application import commands
from application import store


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)
