import re
from app import db
from app.models.search_results import SearchResults
from typing import Optional


COLLECTION_NAME = "articles"


def search(
    value: Optional[str] = None,
    page: Optional[int] = 0,
    limit: Optional[int] = 0,
):
    filter = {"title": re.compile(value, re.IGNORECASE)} if value else {}
    return SearchResults(
        data=db.retrieve_by_attribute(
            COLLECTION_NAME, filter, page=page, limit=limit
        ),
        total_records=db.retrieve_qty_documents(COLLECTION_NAME, filter),
        page=page,
        limit=limit,
    ).to_json()
