import strawberry
from math import ceil
from typing import Optional, TypeVar

GenericType = TypeVar("GenericType")


@strawberry.type
class PageInfo:
    total_records: int
    limit: Optional[int]
    page: Optional[int]

    @strawberry.field
    def total_pages(self) -> int:
        return ceil(self.total_records / self.limit) if self.limit else 0
