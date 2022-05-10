import bson
from pydantic import BaseModel
from pymongo.errors import DuplicateKeyError
from app import db
from typing import Optional, Dict
from app.models.articles import COLLECTION_NAME as ARTICLES_COLLECTION_NAME
from app.models.search_results import SearchResults
from app.errors import (
    ArticleNotFoundError,
    InvalidArticleIDError,
    ReadListItemConflictError,
)


COLLECTION_NAME = "reading_list"


class ReadingListItem(BaseModel):
    article_id: str


def search(page: Optional[int] = 0, limit: Optional[int] = 0) -> Dict:
    return SearchResults(
        data=db.retrieve_by_attribute(COLLECTION_NAME, page=page, limit=limit),
        total_records=db.retrieve_qty_documents(COLLECTION_NAME),
        page=page,
        limit=limit,
    ).to_json()


def add(item: ReadingListItem):
    try:
        article = db.retrieve_by_id(
            ARTICLES_COLLECTION_NAME,
            item.article_id,
        )
        if article:
            db.add_document(COLLECTION_NAME, article)
        else:
            raise ArticleNotFoundError()
    except bson.errors.InvalidId:
        raise InvalidArticleIDError()
    except DuplicateKeyError:
        raise ReadListItemConflictError()


def remove(article_id: str):
    try:
        article = db.retrieve_by_id(
            ARTICLES_COLLECTION_NAME,
            article_id,
        )
        if article:
            db.remove_document(COLLECTION_NAME, article_id)
        else:
            raise ArticleNotFoundError()
    except bson.errors.InvalidId:
        raise InvalidArticleIDError()
