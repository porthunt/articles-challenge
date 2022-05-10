import mongomock
import pytest
from bson import ObjectId
from app.errors import InvalidInputError
from app.controllers import articles
from app import db


@mongomock.patch(servers=(("localhost", 27017),))
def test_search():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b4459")},
    ]
    collection = db.get_collection("articles")
    collection.insert_many(objects)
    search = articles.search()
    assert len(search["data"]) == 2
    assert search["total_pages"] == 0
    assert search["page"] == 1
    assert search["limit"] == 0


@mongomock.patch(servers=(("localhost", 27017),))
def test_search_invalid_page():
    with pytest.raises(InvalidInputError):
        articles.search(page=0)


@mongomock.patch(servers=(("localhost", 27017),))
def test_search_filter():
    objects = [
        {
            "_id": ObjectId("62799f97c6dd2fb89f7b4448"),
            "title": "This is a test",
        },
        {
            "_id": ObjectId("62799f97c6dd2fb89f7b4459"),
            "title": "This is another",
        },
    ]
    collection = db.get_collection("articles")
    collection.insert_many(objects)
    search = articles.search(value="This")
    assert len(search["data"]) == 2
    search = articles.search(value="another")
    assert len(search["data"]) == 1
