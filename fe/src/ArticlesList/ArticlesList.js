import React from "react";
import ArticleTile from "../ArticleTile/ArticleTile";
import SearchArea from "../SearchArea/SearchArea";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import ArticlesPagination from "../ArticlesPagination/ArticlesPagination";

const isInReadingList = (id, readingList) => {
  return readingList.some((article) => article._id.$oid === id);
};

const ArticlesList = (props) => {
  return (
    <Container className="mt-3">
      {props.showSearch ? (
        <SearchArea
          searchSubmit={props.searchSubmit}
          totalRecords={props.articles.totalRecords}
        />
      ) : null}
      <Row md={5}>
        {props.articles.data && props.articles.data.length !== 0 ? (
          props.articles.data.map((article) => {
            return (
              <ArticleTile
                key={article._id.$oid}
                article={article}
                addToReadingList={props.addToReadingList}
                removeFromReadingList={props.removeFromReadingList}
                inReadingList={isInReadingList(
                  article._id.$oid,
                  props.readingList.data
                )}
              />
            );
          })
        ) : (
          <span>Nothing to display.</span>
        )}
      </Row>
      {props.articles.page ? (
        <ArticlesPagination
          page={props.articles.page}
          total={props.articles.totalPages}
          changePage={props.changePage}
          term={props.term}
        />
      ) : null}
    </Container>
  );
};

export default ArticlesList;
