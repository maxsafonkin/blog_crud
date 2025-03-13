from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Post:
    id: int
    title: str
    content: str
    date: datetime

    def to_dict(self) -> dict:
        return asdict(self)
