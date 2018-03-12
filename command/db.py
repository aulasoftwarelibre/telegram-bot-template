# coding=utf-8
from telebot import util
from hackathon import bot
from model import chat


@bot.message_handler(commands=['save'])
def save(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """

    data = util.extract_arguments(message.text)
    if not data:
        bot.reply_to(message, "Debe indicar el dato que quiere que guarde")
        return

    chat_id = message.chat.id
    chat.Chat.set_config(chat_id, 'memory', data)
    bot.reply_to(message, "Dato guardado. Usa /load para recuperar")


@bot.message_handler(commands=['load'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    chat_id = message.chat.id
    data = chat.Chat.get_config(chat_id, 'memory').value
    if not data:
        bot.reply_to(message, "Aún no has guardado nada")
        return

    bot.reply_to(message, "Dato recuperado: %s" % data)
