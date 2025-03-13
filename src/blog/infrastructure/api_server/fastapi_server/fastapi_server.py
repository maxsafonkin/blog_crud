import uvicorn

from blog import usecases
from .app import get_app
from ..api_server import APIServer


class FastAPIServer(APIServer):
    __SERVER_PORT = 30001

    def __init__(self, post_usecases: usecases.PostUsecases) -> None:
        super().__init__(post_usecases=post_usecases)

    def start(self) -> None:
        config = uvicorn.Config(
            app=get_app(self._post_usecases),
            host="0.0.0.0",
            port=self.__SERVER_PORT,
        )
        server = uvicorn.Server(config)
        server.run()
