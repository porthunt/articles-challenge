from fastapi import APIRouter
from typing import Optional
from app.models.articles import search


router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/")
def retrieve_articles(
    term: Optional[str] = None,
    page: Optional[int] = 0,
    limit: Optional[int] = 100,
):
    return search(term, page=page, limit=limit)
