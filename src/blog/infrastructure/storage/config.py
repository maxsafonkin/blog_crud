from dataclasses import dataclass


@dataclass(frozen=True)
class StorageConfig:
    host: str
    port: int
    username: str
    password: str
    db_name: str
