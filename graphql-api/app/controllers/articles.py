from app import db
from app.errors import InvalidInputError
from typing import Optional, Tuple, List, Dict


COLLECTION_NAME = "articles"


def search(
    value: Optional[str] = None,
    page: Optional[int] = 1,
    limit: Optional[int] = 20,
) -> Tuple[List[Dict], int]:
    if page < 1 or limit < 1:
        raise InvalidInputError(
            "page and limit must be greater or equal than 1"
        )
    filter = (
        {"title": {"$regex": f"(?i)\\b{value}\\b", "$options": "i"}}
        if value
        else {}
    )
    return (
        db.retrieve_by_attribute(
            COLLECTION_NAME, filter, page=page, limit=limit
        ),
        db.retrieve_qty_documents(COLLECTION_NAME, filter),
    )
