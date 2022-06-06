import strawberry
from app.models.article import Article, get_articles
from app.models import bookmark
from typing import List


@strawberry.type
class Query:
    articles: List[Article] = strawberry.field(resolver=get_articles)
    bookmarks: List[Article] = strawberry.field(
        resolver=bookmark.get_bookmarks
    )


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_bookmark(self, article_id: str) -> Article:
        return bookmark.add(article_id)

    @strawberry.mutation
    def remove_bookmark(self, article_id: str) -> Article:
        return bookmark.remove(article_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)
