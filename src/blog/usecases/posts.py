from blog import entities
from . import interfaces


class PostUsecases:
    def __init__(self, storage: interfaces.Storage):
        self._storage = storage

    def create_post(self, title: str, content: str) -> int:
        return self._storage.create_post(title=title, content=content)

    def delete_post(self, id: int) -> None:
        self._storage.delete_post(id=id)

    def update_post_title(self, id: int, title: str) -> None:
        self._storage.update_post_title(id=id, title=title)

    def update_post_content(self, id: int, content: str) -> None:
        self._storage.update_post_content(id=id, content=content)

    def get_post_ids(self) -> list[int]:
        return self._storage.get_post_ids()

    def get_post(self, id: int) -> entities.Post:
        return self._storage.get_post(id=id)
