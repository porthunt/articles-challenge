import bson
from pymongo.errors import DuplicateKeyError
from app import db
from typing import Dict
from app.controllers.articles import (
    COLLECTION_NAME as ARTICLES_COLLECTION_NAME,
)
from app.models.search_results import SearchResults
from app.errors import (
    ArticleNotFoundError,
    InvalidArticleIDError,
    ReadListItemConflictError,
)
from app.models.reading_list import ReadingListItem


COLLECTION_NAME = "reading_list"


def search() -> Dict:
    return SearchResults(
        data=db.retrieve_by_attribute(COLLECTION_NAME),
        total_records=db.retrieve_qty_documents(COLLECTION_NAME),
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
