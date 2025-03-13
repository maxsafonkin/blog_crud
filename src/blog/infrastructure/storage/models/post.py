from dataclasses import asdict, dataclass
from datetime import datetime

from blog import entities


@dataclass
class Post:
    id: int
    title: str
    content: str
    date: datetime

    def to_entity(self) -> entities.Post:
        return entities.Post(**asdict(self))
