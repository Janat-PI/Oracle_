from typing import TypedDict
from environs import Env


class DjangoSettings(TypedDict):

    SECRET_KEY: str
    DEBUG: bool

env = Env()
env.read_env(".env")

django_settings = DjangoSettings(
    SECRET_KEY=env("SECRET_KEY"),
    DEBUG=env.bool("DEBUG")
)