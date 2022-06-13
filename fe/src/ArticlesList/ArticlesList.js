import React from "react";
import ArticleTile from "../ArticleTile/ArticleTile";
import SearchArea from "../SearchArea/SearchArea";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import ArticlesPagination from "../ArticlesPagination/ArticlesPagination";

const isInReadingList = (id, readingList) => {
  return readingList.some((article) => article.Id === id);
};

const ArticlesList = (props) => {
  return (
    <Container className="mt-3">
      {props.showSearch ? (
        <SearchArea
          searchSubmit={props.searchSubmit}
          totalRecords={props.articles.pageInfo.totalRecords}
        />
      ) : null}
      <Row md={5}>
        {props.articles.data && props.articles.data.length !== 0 ? (
          props.articles.data.map((article) => {
            return (
              <ArticleTile
                key={article.Id}
                article={article}
                addToReadingList={props.addToReadingList}
                removeFromReadingList={props.removeFromReadingList}
                inReadingList={isInReadingList(
                  article.Id,
                  props.readingList.data
                )}
              />
            );
          })
        ) : (
          <span>Nothing to display.</span>
        )}
      </Row>
      {props.articles.pageInfo.page ? (
        <ArticlesPagination
          page={props.articles.pageInfo.page}
          total={props.articles.pageInfo.totalPages}
          changePage={props.changePage}
          term={props.term}
        />
      ) : null}
    </Container>
  );
};

export default ArticlesList;
