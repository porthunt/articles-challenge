from pydantic import BaseModel


class ReadingListItem(BaseModel):
    article_id: str
