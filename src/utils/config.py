from dataclasses import dataclass

from . import environment as env


@dataclass
class Config:
    storage_config: dict


def load_config() -> Config:
    storage_config = {
        "host": env.DB_HOST,
        "port": env.DB_PORT,
        "username": env.DB_USER,
        "password": env.DB_PASSWORD,
        "db_name": env.DB_NAME,
    }
    config = Config(storage_config=storage_config)
    return config
