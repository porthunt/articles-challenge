import React from 'react';
import './ArticlesList.css';
import ArticleTile from '../ArticleTile/ArticleTile';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ArticlesPagination from '../ArticlesPagination/ArticlesPagination';


const isInReadingList = (id, readingList) => {
    return readingList.some(article => article._id.$oid === id);
}

const ArticlesList = (props) => {
        return (
            <Container className="mt-3">
                {props.showSearch ? 
                    <form onSubmit={(e) => props.searchSubmit(e)}>
                    <input className="form-control" type="text" placeholder="Search term" aria-label="Search term" />
                        <button className="d-none" type="submit"></button>
                    </form> :
                null
                }
                <span>Records found: {props.articles.total_records}</span>
                <Row md={5}>
                    {props.articles.data && props.articles.data.length !== 0 ?
                        props.articles.data.map((article) => {
                            return (
                                <ArticleTile
                                    key={article._id.$oid}
                                    article={article}
                                    addToReadingList={props.addToReadingList}
                                    removeFromReadingList={props.removeFromReadingList}
                                    inReadingList={isInReadingList(article._id.$oid, props.readingList.data)} />
                            )
                        }) :
                        <span>Nothing to display.</span>
                    }
                </Row>
            {props.articles.page ? 
                <ArticlesPagination
                page={props.articles.page}
                total={props.articles.total_pages}
                changePage={props.changePage}
                term={props.term} /> :
                null}
            </Container>
        );
}

export default ArticlesList;