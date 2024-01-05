from pydantic import BaseModel

from ..infrastructure.orm import Settings, Settings_Pydantic


class LoadSettingCommand(BaseModel):
    chat: int
    key: str


class LoadSettingHandler:
    def __init__(self, settings: type[Settings]) -> None:
        self.settings = settings

    async def handle(self, command: LoadSettingCommand) -> str:
        setting_obj = await Settings_Pydantic.from_queryset_single(
            self.settings.get(chat=command.chat, key=command.key)
        )

        return setting_obj.value  # type: ignore
