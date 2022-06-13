import ArticlesList from "./ArticlesList/ArticlesList";
import Menu from "./Menu/Menu";
import { useState, useEffect } from "react";
import { API_ENDPOINT, QUERIES } from "./Api";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [articles, setArticles] = useState({ data: [], pageInfo: {} });
  const [readingList, setReadingList] = useState({ data: [], pageInfo: {} });
  const [searchTerm, setSearchTerm] = useState("");
  const [displayed, setDisplayed] = useState("articles");
  const [currentPage, setCurrentPage] = useState(1);

  const retrieveArticles = (term, page) => {
    setSearchTerm(term);
    setCurrentPage(page);
    return axios
      .post(API_ENDPOINT, {query: QUERIES.articles, variables: {"page": page, "limit": 10, "term": term}})
      .then((res) => {
        setArticles(res.data.data.articles);
      })
      .catch((err) => {
        console.log(err);
        return [];
      });
  };

  const retrieveReadingList = () => {
    return axios
      .post(API_ENDPOINT, {query: QUERIES.bookmarks})
      .then((res) => {
        setReadingList(res.data.data.bookmarks);
      })
      .catch((err) => {
        console.log(err);
        return [];
      });
  };

  const addToReadingList = (id) => {
    axios
      .post(API_ENDPOINT, {query: QUERIES.addBookmark, variables: {"articleId": id}})
      .then((_) => {
        retrieveReadingList();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const removeFromReadingList = (id) => {
    axios
      .post(API_ENDPOINT, {query: QUERIES.removeBookmark, variables: {"articleId": id}})
      .then((_) => {
        retrieveReadingList();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const changeDisplay = (type) => {
    setDisplayed(type);
    if (type === "articles") {
      retrieveArticles("", currentPage);
    } else {
      retrieveReadingList();
    }
  };

  const search = (e) => {
    e.preventDefault();
    retrieveArticles(e.target[0].value, 1);
  };

  useEffect(() => {
    retrieveArticles("", 1);
    retrieveReadingList();
  }, []);

  return (
    <div className="App">
      <Menu changeDisplay={changeDisplay} />
      <ArticlesList
        searchSubmit={search}
        articles={displayed === "articles" ? articles : readingList}
        showSearch={displayed === "articles"}
        changePage={
          displayed === "articles" ? retrieveArticles : retrieveReadingList
        }
        term={searchTerm}
        addToReadingList={addToReadingList}
        removeFromReadingList={removeFromReadingList}
        readingList={readingList}
      />
    </div>
  );
};

export default App;
