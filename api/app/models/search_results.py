from pydantic import BaseModel
from math import ceil
from typing import Dict, Optional, List


class SearchResults(BaseModel):
    data: Optional[List[Dict]]
    total_records: int
    page: int
    limit: int

    def to_json(self):
        return {
            "data": self.data,
            "total_pages": ceil(self.total_records / self.limit)
            if self.limit
            else 0,
            "page": self.page,
            "limit": self.limit,
        }
