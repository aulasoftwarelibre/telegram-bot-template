from ..infrastructure.orm import Settings
from .load_setting import LoadSettingCommand, LoadSettingHandler
from .save_setting import SaveSettingCommand, SaveSettingHandler

save_setting_handler = SaveSettingHandler(Settings)
load_setting_handler = LoadSettingHandler(Settings)


async def save_setting(command: SaveSettingCommand) -> None:
    await save_setting_handler.handle(command)


async def load_setting(command: LoadSettingCommand) -> str:
    return await load_setting_handler.handle(command)


__all__ = [
    "LoadSettingCommand",
    "SaveSettingCommand",
    "load_settign",
    "save_setting",
]
