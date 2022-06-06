import bson

from app import db, errors
from app.controllers.bookmarks import search
from app.models.article import Article, generate_article
from pymongo.errors import DuplicateKeyError
from app.controllers.articles import (
    COLLECTION_NAME as ARTICLES_COLLECTION_NAME,
)
from app.controllers.bookmarks import COLLECTION_NAME
from app.models.page_info import Connection, PageInfo


def get_bookmarks() -> Connection[Article]:
    results, qty = search()
    articles = [generate_article(a) for a in results]
    return Connection(
        page_info=PageInfo(
            total_records=qty,
            limit=None,
            page=None,
        ),
        data=articles,
    )


def add(article_id: str) -> Article:
    try:
        article = db.retrieve_by_id(
            ARTICLES_COLLECTION_NAME,
            article_id,
        )
        if article:
            db.add_document(COLLECTION_NAME, article)
            return generate_article(article)
        else:
            raise errors.ArticleNotFoundError()
    except bson.errors.InvalidId:
        raise errors.InvalidArticleIDError()
    except DuplicateKeyError:
        raise errors.ReadListItemConflictError()


def remove(article_id: str):
    try:
        article = db.retrieve_by_id(
            ARTICLES_COLLECTION_NAME,
            article_id,
        )
        if article:
            db.remove_document(COLLECTION_NAME, article_id)
            return generate_article(article)
        else:
            raise errors.ArticleNotFoundError()
    except bson.errors.InvalidId:
        raise errors.InvalidArticleIDError()
