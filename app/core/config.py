from os import getenv
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent
print(BASE_DIR)


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    # db_echo: bool = False
    db_echo: bool = True


settings = Settings()
