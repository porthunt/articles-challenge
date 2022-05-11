import mongomock
import pytest
from bson import ObjectId
from app.controllers import reading_list
from app.models.reading_list import ReadingListItem
from app.errors import ArticleNotFoundError, InvalidArticleIDError
from app import db


@mongomock.patch(servers=(("localhost", 27017),))
def test_search():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b4459")},
    ]
    collection = db.get_collection("reading_list")
    collection.insert_many(objects)
    search = reading_list.search()
    assert len(search["data"]) == 2
    assert search["totalRecords"] == 2


@mongomock.patch(servers=(("localhost", 27017),))
def test_add():
    article_id = "62799f97c6dd2fb89f7b4448"
    article = {"_id": ObjectId(article_id)}
    articles_collection = db.get_collection("articles")
    rl_collection = db.get_collection("reading_list")
    articles_collection.insert_one(article)
    assert len(list(rl_collection.find({}))) == 0
    reading_list.add(ReadingListItem(article_id=article_id))
    results = list(rl_collection.find({}))
    assert len(results) == 1
    assert results[0]["_id"] == ObjectId(article_id)


@mongomock.patch(servers=(("localhost", 27017),))
def test_add_article_not_found():
    article_id = "62799f97c6dd2fb89f7b4448"
    with pytest.raises(ArticleNotFoundError):
        reading_list.add(ReadingListItem(article_id=article_id))


@mongomock.patch(servers=(("localhost", 27017),))
def test_add_article_invalid_article_id():
    article_id = "xxx"
    with pytest.raises(InvalidArticleIDError):
        reading_list.add(ReadingListItem(article_id=article_id))


@mongomock.patch(servers=(("localhost", 27017),))
def test_remove():
    article_id = "62799f97c6dd2fb89f7b4448"
    article = {"_id": ObjectId(article_id)}
    articles_collection = db.get_collection("articles")
    rl_collection = db.get_collection("reading_list")
    articles_collection.insert_one(article)
    rl_collection.insert_one({"_id": ObjectId(article_id)})
    assert len(list(rl_collection.find({}))) == 1
    reading_list.remove(article_id)
    assert len(list(rl_collection.find({}))) == 0


@mongomock.patch(servers=(("localhost", 27017),))
def test_remove_article_not_found():
    fake_id = "62799f97c6dd2fb89f7b4448"
    with pytest.raises(ArticleNotFoundError):
        reading_list.remove(fake_id)


@mongomock.patch(servers=(("localhost", 27017),))
def test_remove_article_invalid_article_id():
    fake_id = "xxx"
    with pytest.raises(InvalidArticleIDError):
        reading_list.remove(fake_id)
