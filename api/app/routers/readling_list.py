from fastapi import APIRouter
from app.controllers.reading_list import search, add, remove
from app.models.reading_list import ReadingListItem
from app.errors import Error, UnknownError


router = APIRouter(prefix="/reading-list", tags=["reading-list"])


@router.get("/")
def retrieve_reading_list():
    return search()


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
