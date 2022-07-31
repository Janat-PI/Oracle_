from typing import TypedDict
from environs import Env


class DjangoSettings(TypedDict):

    SECRET_KEY: str
    DEBUG: bool


class DatabaseSettings(TypedDict):

    EMAIL_BACKEND: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str


env = Env()
env.read_env(".env")

django_settings = DjangoSettings(
    SECRET_KEY=env("SECRET_KEY"),
    DEBUG=env.bool("DEBUG")
)

database_settings = DatabaseSettings(
    EMAIL_BACKEND = env("EMAIL_BACKEND"),
    EMAIL_HOST = env("EMAIL_HOST"),
    EMAIL_PORT = env.int("EMAIL_PORT"),
    EMAIL_HOST_USER = env("EMAIL_HOST_USER"),
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD"),
)