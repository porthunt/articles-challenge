import strawberry
from app.models.article import Article
from app.models.page_info import PageInfo
from app.controllers.articles import search
from typing import List, TypeVar, Generic

MongoDocument = TypeVar("MongoDocument")


@strawberry.type
class Connection(Generic[MongoDocument]):
    page_info: PageInfo
    data: List[MongoDocument]


def get_articles(page: int = 1, limit: int = 10) -> Connection[Article]:
    results, qty = search(None, page=page, limit=limit)
    articles = [
        Article(
            _id=a["_id"]["$oid"],
            cord_uid=a["cord_uid"],
            sha=a["sha"],
            source_x=a["source_x"],
            title=a["title"],
            doi=a["doi"],
            pmcid=a["pmcid"],
            pubmed_id=a["pubmed_id"],
            license=a["license"],
            abstract=a["abstract"],
            publish_time=a["publish_time"],
            authors=a["authors"],
            journal=a["journal"],
            microsoft_academic_paper_id=a["Microsoft Academic Paper ID"],
            who_covidence=a["WHO #Covidence"],
            has_pdf_parse=a["has_pdf_parse"] == "True",
            has_pmc_xml_parse=a["has_pmc_xml_parse"] == "True",
            full_text_file=a["full_text_file"],
            url=a["url"],
        )
        for a in results
    ]

    return Connection(
        page_info=PageInfo(
            total_records=qty,
            limit=limit,
            page=page,
        ),
        data=articles,
    )


@strawberry.type
class Query:
    articles: List[Article] = strawberry.field(resolver=get_articles)


schema = strawberry.Schema(query=Query)
