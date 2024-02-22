import logging

import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from ..config import settings

bot = AsyncTeleBot(settings.bot_token)
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=["start"])  # type: ignore
async def start(message: Message) -> None:
    await bot.reply_to(message, "Hello, " + message.from_user.first_name)


@bot.message_handler(func=lambda message: True)  # type: ignore # noqa: ARG005
async def echo_message(message: Message) -> None:
    await bot.reply_to(message, message.text)
