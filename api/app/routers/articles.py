from fastapi import APIRouter
from typing import Optional, List, Dict
from app.controllers.articles import search
from app.errors import Error, UnknownError


router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/")
def retrieve_articles(
    term: Optional[str] = None,
    page: Optional[int] = 1,
    limit: Optional[int] = 20,
) -> List[Dict]:
    try:
        return search(term, page=page, limit=limit)
    except Exception as e:
        if isinstance(e, Error):
            raise e.http_exception()
        else:
            raise UnknownError().http_exception()
