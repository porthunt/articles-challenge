from pydantic import BaseModel
from math import ceil
from typing import Dict, Optional, List


class SearchResults(BaseModel):
    data: Optional[List[Dict]]
    total_records: int
    page: Optional[int] = 0
    limit: Optional[int]

    def to_json(self):
        response = {
            "data": self.data,
            "total_records": self.total_records,
        }
        if self.page > 0:
            response["total_pages"] = (
                ceil(self.total_records / self.limit) if self.limit else 0
            )
            response["page"] = self.page
            response["limit"] = self.limit
        return response
