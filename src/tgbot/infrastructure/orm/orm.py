from tortoise import Tortoise

from ..config import settings


async def init() -> None:
    await Tortoise.init(
        db_url=settings.database_url,
        modules={
            "models": [
                "tgbot.infrastructure.orm",
            ]
        },
    )


async def setup() -> None:
    await init()
    await Tortoise.generate_schemas()
