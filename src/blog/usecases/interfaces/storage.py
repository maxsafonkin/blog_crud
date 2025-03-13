import abc

from blog.entities import Post


class Storage(abc.ABC):
    @abc.abstractmethod
    def create_post(self, title: str, content: str) -> int:
        pass

    @abc.abstractmethod
    def delete_post(self, id: int) -> None:
        pass

    @abc.abstractmethod
    def update_post_title(self, id: int, title: str) -> None:
        pass

    @abc.abstractmethod
    def update_post_content(self, id: int, content: str) -> None:
        pass

    @abc.abstractmethod
    def get_post_ids(self) -> list[int]:
        pass

    @abc.abstractmethod
    def get_post(self, id: int) -> Post:
        pass
