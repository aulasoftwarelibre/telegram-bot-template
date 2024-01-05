import telebot
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from ..bot import bot
from ..config import settings

app = FastAPI()

register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": ["tgbot.infrastructure.orm"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post(f"/{settings.secret_token}/")
async def process_webhook(update: dict[str, object]) -> None:
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        await bot.process_new_updates([update])
    else:
        return


def main() -> None:
    uvicorn.run(
        "tgbot.infrastructure.api:app",
        host="0.0.0.0",  # noqa: S104
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
