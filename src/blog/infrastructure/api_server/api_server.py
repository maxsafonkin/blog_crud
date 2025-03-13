import abc

from blog import usecases


class APIServer(abc.ABC):
    def __init__(self, post_usecases: usecases.PostUsecases) -> None:
        self._post_usecases = post_usecases

    @abc.abstractmethod
    def start(self) -> None:
        pass
