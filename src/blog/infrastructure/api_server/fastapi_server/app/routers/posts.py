from fastapi import APIRouter

from blog import usecases


router = APIRouter(prefix="/posts")
post_usecases: usecases.PostUsecases = None


@router.get("/ids")
def get_post_ids():
    return post_usecases.get_post_ids()


@router.get("/{id}")
def get_post(id: int):
    return post_usecases.get_post(id).to_dict()


@router.post("/create")
def create_post(title: str, content: str) -> int:
    return post_usecases.create_post(title=title, content=content)


@router.delete("/{id}")
def delete_post(id: int):
    post_usecases.delete_post(id=id)


@router.patch("/{id}/update/title")
def update_post_title(id: int, title: str):
    post_usecases.update_post_title(id=id, title=title)


@router.patch("/{id}/update/content")
def update_post_content(id: int, content: str):
    post_usecases.update_post_content(id=id, content=content)
