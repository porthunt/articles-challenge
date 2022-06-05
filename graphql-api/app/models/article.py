import strawberry
from typing import Optional


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
