from tortoise import fields
from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from tortoise.models import Model


class Settings(Model):
    id = fields.IntField(pk=True)
    chat = fields.BigIntField()
    key = fields.CharField(max_length=255)
    value = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


Settings_Pydantic: PydanticModel = pydantic_model_creator(Settings, name="Settings")  # type: ignore
