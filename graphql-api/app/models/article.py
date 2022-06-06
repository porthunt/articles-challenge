import strawberry
from typing import Optional, Dict
from app.controllers.articles import search
from app.models.page_info import Connection, PageInfo


@strawberry.type
class Article:
    _id: strawberry.ID
    cord_uid: str
    sha: Optional[str]
    source_x: Optional[str]
    title: Optional[str]
    doi: Optional[str]
    pmcid: Optional[str]
    pubmed_id: Optional[str]
    license: Optional[str]
    abstract: Optional[str]
    publish_time: Optional[str]
    authors: Optional[str]
    journal: Optional[str]
    microsoft_academic_paper_id: Optional[str]
    who_covidence: Optional[str]
    has_pdf_parse: Optional[bool]
    has_pmc_xml_parse: Optional[bool]
    full_text_file: Optional[str]
    url: Optional[str]


def generate_article(data: Dict) -> Article:
    try:
        _id = data["_id"]["$oid"]
    except TypeError:
        _id = str(data["_id"])

    return Article(
        _id=_id,
        cord_uid=data["cord_uid"],
        sha=data["sha"],
        source_x=data["source_x"],
        title=data["title"],
        doi=data["doi"],
        pmcid=data["pmcid"],
        pubmed_id=data["pubmed_id"],
        license=data["license"],
        abstract=data["abstract"],
        publish_time=data["publish_time"],
        authors=data["authors"],
        journal=data["journal"],
        microsoft_academic_paper_id=data["Microsoft Academic Paper ID"],
        who_covidence=data["WHO #Covidence"],
        has_pdf_parse=data["has_pdf_parse"] == "True",
        has_pmc_xml_parse=data["has_pmc_xml_parse"] == "True",
        full_text_file=data["full_text_file"],
        url=data["url"],
    )


def get_articles(
    title: str = None, page: int = 1, limit: int = 10
) -> Connection[Article]:
    results, qty = search(title, page=page, limit=limit)
    articles = [generate_article(a) for a in results]

    return Connection(
        page_info=PageInfo(
            total_records=qty,
            limit=limit,
            page=page,
        ),
        data=articles,
    )
