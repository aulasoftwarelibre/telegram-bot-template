from pydantic import BaseModel

from ..infrastructure.orm import Settings


class SaveSettingCommand(BaseModel):
    chat: int
    key: str
    value: str


class SaveSettingHandler:
    def __init__(self, settings: type[Settings]) -> None:
        self.settings = settings

    async def handle(self, command: SaveSettingCommand) -> None:
        await self.settings.create(**command.model_dump())
