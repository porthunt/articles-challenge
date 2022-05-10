import json
import pymongo
from bson import json_util, ObjectId
from typing import Dict, Optional
from app.settings import MONGODB_INFO
from app.errors import DBUnreachableError


def get_collection(collection: str) -> pymongo.collection.Collection:
    client = pymongo.MongoClient(
        host=MONGODB_INFO["host"],
        port=MONGODB_INFO["port"],
        serverSelectionTimeoutMS=MONGODB_INFO["timeout"],
        connectTimeoutMS=MONGODB_INFO["timeout"],
    )
    DB_CONN = client[MONGODB_INFO["db_name"]]
    return DB_CONN[collection]


def add_document(collection_name: str, attributes: dict) -> str:
    collection = get_collection(collection_name)
    try:
        return str(collection.insert_one(attributes).inserted_id)
    except pymongo.errors.ServerSelectionTimeoutError:
        raise DBUnreachableError()


def remove_document(collection_name: str, _id: str):
    collection = get_collection(collection_name)
    try:
        collection.delete_one({"_id": ObjectId(_id)})
    except pymongo.errors.ServerSelectionTimeoutError:
        raise DBUnreachableError()


def retrieve_by_attribute(
    collection_name: str,
    filter: Optional[Dict[str, str]] = None,
    page: Optional[int] = 0,
    limit: Optional[int] = 0,
):
    filter = filter if filter else {}
    collection = get_collection(collection_name)
    try:
        results = collection.find(filter).skip(limit * page).limit(limit)
        return json.loads(json_util.dumps(results))
    except pymongo.errors.ServerSelectionTimeoutError:
        raise DBUnreachableError()


def retrieve_by_id(collection_name: str, _id: str) -> Optional[Dict]:
    collection = get_collection(collection_name)
    results = collection.find_one({"_id": ObjectId(_id)})
    return results


def retrieve_qty_documents(
    collection_name: str, filter: Optional[Dict[str, str]] = None
) -> int:
    filter = filter if filter else {}
    collection = get_collection(collection_name)
    try:
        return collection.count_documents(filter)
    except pymongo.errors.ServerSelectionTimeoutError:
        raise DBUnreachableError()
