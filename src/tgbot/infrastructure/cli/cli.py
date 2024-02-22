import json
import logging
import sys

import typer
from rich import print, print_json

from tgbot.infrastructure.cli.AsyncTyper import AsyncTyper

from ..bot import bot
from ..config import settings

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


app = AsyncTyper()


@app.command()
def about() -> None:
    typer.echo("This is a bot created from aulasoftwarelibre/telegram-bot-template")


@app.async_command()
async def info() -> None:
    """Returns information about the bot."""
    result = await bot.get_me()
    print("Bot me information")
    print_json(result.to_json())
    result = await bot.get_webhook_info()
    print("Bot webhook information")
    print_json(
        json.dumps(
            {
                "url": result.url,
                "has_custom_certificate": result.has_custom_certificate,
                "pending_update_count": result.pending_update_count,
                "ip_address": result.ip_address,
                "last_error_date": result.last_error_date,
                "last_error_message": result.last_error_message,
                "last_synchronization_error_date": result.last_synchronization_error_date,
                "max_connections": result.max_connections,
                "allowed_updates": result.allowed_updates,
            }
        )
    )
    await bot.close_session()


@app.async_command()
async def install() -> None:
    """Install bot webhook"""
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    await bot.remove_webhook()

    WEBHOOK_URL_BASE = f"https://{settings.webhook_host}:{443}"
    WEBHOOK_URL_PATH = f"/{settings.secret_token}/"

    # Set webhook
    result = await bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

    print(f"Set webhook to {WEBHOOK_URL_BASE + WEBHOOK_URL_PATH}: {result}")

    await bot.close_session()


@app.async_command()
async def serve() -> None:
    """Run polling bot version."""
    logging.info("Starting...")

    await bot.remove_webhook()
    await bot.infinity_polling(logger_level=logging.INFO)

    await bot.close_session()


@app.async_command()
async def uninstall() -> None:
    """Uninstall bot webhook."""
    await bot.remove_webhook()

    await bot.close_session()


if __name__ == "__main__":
    app()
