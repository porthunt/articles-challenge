import strawberry
from math import ceil
from typing import Optional, TypeVar, List, TypeVar, Generic


MongoDocument = TypeVar("MongoDocument")


@strawberry.type
class PageInfo:
    total_records: int
    limit: Optional[int]
    page: Optional[int]

    @strawberry.field
    def total_pages(self) -> int:
        return ceil(self.total_records / self.limit) if self.limit else 0


@strawberry.type
class Connection(Generic[MongoDocument]):
    page_info: PageInfo
    data: List[MongoDocument]
