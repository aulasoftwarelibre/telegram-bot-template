from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    database_url: str
    secret_token: str
    webhook_host: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
