from fastapi import APIRouter
from typing import Optional
from app.models.reading_list import search, ReadingListItem, add, remove
from app.errors import Error, UnknownError


router = APIRouter(prefix="/reading-list", tags=["reading-list"])


@router.get("/")
def retrieve_reading_list(
    page: Optional[int] = 0,
    limit: Optional[int] = 100,
):
    return search(page=page, limit=limit)


@router.post("/", status_code=201)
def add_to_reading_list(item: ReadingListItem):
    try:
        add(item)
    except Exception as e:
        if isinstance(e, Error):
            raise e.http_exception()
        else:
            raise UnknownError().http_exception()


@router.delete("/{article_id}", status_code=204)
def remove_from_reading_list(article_id: str):
    try:
        remove(article_id)
    except Exception as e:
        if isinstance(e, Error):
            raise e.http_exception()
        else:
            raise UnknownError().http_exception()
