import ArticlesList from "./ArticlesList/ArticlesList";
import Menu from "./Menu/Menu";
import { useState, useEffect } from "react";
import { endpoints } from "./Api";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [articles, setArticles] = useState({ data: [] });
  const [readingList, setReadingList] = useState({ data: [] });
  const [searchTerm, setSearchTerm] = useState("");
  const [displayed, setDisplayed] = useState("articles");
  const [currentPage, setCurrentPage] = useState(1);

  const retrieveArticles = (term, page) => {
    setSearchTerm(term);
    setCurrentPage(page);
    return axios
      .get(`${endpoints.getArticles}?term=${term}&limit=10&page=${page}`)
      .then((res) => {
        setArticles(res.data);
      })
      .catch((err) => {
        console.log(err);
        return [];
      });
  };

  const retrieveReadingList = () => {
    return axios
      .get(`${endpoints.readingList}`)
      .then((res) => {
        setReadingList(res.data);
      })
      .catch((err) => {
        console.log(err);
        return [];
      });
  };

  const addToReadingList = (id) => {
    axios
      .post(`${endpoints.readingList}`, { article_id: id })
      .then((_) => {
        retrieveReadingList();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const removeFromReadingList = (id) => {
    axios
      .delete(`${endpoints.readingList}/${id}`)
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
