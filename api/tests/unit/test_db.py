import mongomock
from bson import ObjectId
from app import db


COLLECTION = "collection"


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_by_id():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a")},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    document = db.retrieve_by_id(COLLECTION, "62799f97c6dd2fb89f7b4448")
    assert document["_id"] == ObjectId("62799f97c6dd2fb89f7b4448")


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_qty_documents():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b664a")},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    db.retrieve_qty_documents(COLLECTION) == 3


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_qty_documents_with_filters():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448"), "name": "foo"},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a"), "name": "foo"},
        {"_id": ObjectId("62799f97c6dd2fb89f7b664a"), "name": "bar"},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    db.retrieve_qty_documents(COLLECTION, {"name": "foo"}) == 2


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_by_attribute_with_filters():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448"), "name": "foo"},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a"), "name": "foo"},
        {"_id": ObjectId("62799f97c6dd2fb89f7b664a"), "name": "bar"},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    documents = db.retrieve_by_attribute(COLLECTION, {"name": "bar"})
    assert len(documents) == 1
    assert documents[0]["_id"]["$oid"] == "62799f97c6dd2fb89f7b664a"


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_by_attribute_no_filters_limitation():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b664a")},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    documents = db.retrieve_by_attribute(COLLECTION)
    assert len(documents) == 3
    documents = db.retrieve_by_attribute(COLLECTION, limit=1)
    assert len(documents) == 1


@mongomock.patch(servers=(("localhost", 27017),))
def test_retrieve_by_attribute_no_filters_pagination():
    objects = [
        {"_id": ObjectId("62799f97c6dd2fb89f7b4448")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b444a")},
        {"_id": ObjectId("62799f97c6dd2fb89f7b664a")},
    ]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    documents = db.retrieve_by_attribute(COLLECTION)
    assert len(documents) == 3
    documents = db.retrieve_by_attribute(COLLECTION, page=1, limit=1)
    assert documents[0]["_id"]["$oid"] == "62799f97c6dd2fb89f7b4448"
    documents = db.retrieve_by_attribute(COLLECTION, page=2, limit=1)
    assert documents[0]["_id"]["$oid"] == "62799f97c6dd2fb89f7b444a"
    documents = db.retrieve_by_attribute(COLLECTION, page=3, limit=1)
    assert documents[0]["_id"]["$oid"] == "62799f97c6dd2fb89f7b664a"


@mongomock.patch(servers=(("localhost", 27017),))
def test_add_document():
    collection = db.get_collection(COLLECTION)
    fake_id = "62799f97c6dd2fb89f7b4453"
    assert len(list(collection.find({}))) == 0
    db.add_document(COLLECTION, {"_id": ObjectId(fake_id)})
    assert len(list(collection.find({"_id": ObjectId(fake_id)}))) == 1


@mongomock.patch(servers=(("localhost", 27017),))
def test_remove_document():
    fake_id = "62799f97c6dd2fb89f7b4555"
    objects = [{"_id": ObjectId(fake_id)}]
    collection = db.get_collection(COLLECTION)
    collection.insert_many(objects)
    assert len(list(collection.find({"_id": ObjectId(fake_id)}))) == 1
    db.remove_document(COLLECTION, fake_id)
    assert len(list(collection.find({"_id": ObjectId(fake_id)}))) == 0
