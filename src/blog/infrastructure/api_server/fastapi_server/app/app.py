from fastapi import FastAPI

from blog import usecases
from . import routers


def get_app(post_usecases: usecases.PostUsecases) -> FastAPI:
    app = FastAPI()

    routers.posts.post_usecases = post_usecases

    app.include_router(routers.posts.router, prefix="/api/v1")

    return app
