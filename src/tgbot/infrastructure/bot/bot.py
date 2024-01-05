import logging

import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from ...application import (
    LoadSettingCommand,
    SaveSettingCommand,
    load_setting,
    save_setting,
)
from ..config import settings

bot = AsyncTeleBot(settings.bot_token)
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=["start"])  # type: ignore
async def start(message: Message) -> None:
    await bot.reply_to(message, "Hello, " + message.from_user.first_name)


@bot.message_handler(commands=["save"])  # type: ignore
async def save(message: Message) -> None:
    """
    Guarda un dato en el chat que se puede recuperar después
    """

    data = telebot.util.extract_arguments(message.text)
    if not data:
        await bot.reply_to(message, "Debe indicar el dato que quiere que guarde")
        return

    chat_id = message.chat.id
    await save_setting(SaveSettingCommand(chat=chat_id, key="memory", value=data))
    await bot.reply_to(message, "Dato guardado. Usa /load para recuperar")


@bot.message_handler(commands=["load"])  # type: ignore
async def load(message: Message) -> None:
    """
    Recupera un dato guardado con save
    """

    chat_id = message.chat.id
    data = await load_setting(LoadSettingCommand(chat=chat_id, key="memory"))
    if not data:
        await bot.reply_to(message, "Aún no has guardado nada")
        return

    await bot.reply_to(message, "Dato recuperado: %s" % data)


@bot.message_handler(func=lambda message: True)  # type: ignore # noqa: ARG005
async def echo_message(message: Message) -> None:
    await bot.reply_to(message, message.text)
