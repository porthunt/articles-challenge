import './App.css';
import ArticlesList from './ArticlesList/ArticlesList';
import Menu from './Menu/Menu';
import { useState, useEffect } from 'react';
import { endpoints } from './Api';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {

  const [articles, setArticles] = useState({"data": []});
  const [readingList, setReadingList] = useState({"data": []});
  const [totalRecords, setTotalRecords] = useState("");
  const [page, setPage] = useState(0);
  const [totalPages, setTotalPages] = useState(0);
  const [search_term, setSearchTerm] = useState("");
  const [displayed, setDisplayed] = useState("articles");
  

  const retrieveArticles = (term, page) => {
    setSearchTerm(term);
    return axios.get(`${endpoints.get_articles}?term=${term}&limit=10&page=${page}`)
      .then(res => {
        setArticles(res.data);
        setTotalRecords(res.data.total_records);
        setPage(res.data.page);
        setTotalPages(res.data.total_pages);
      })
      .catch(err => {
        console.log(err);
        return [];
      });
  }

  const retrieveReadingList = (page) => {
    return axios.get(`${endpoints.reading_list}`)
      .then(res => {
        setReadingList(res.data);
      })
      .catch(err => {
        console.log(err);
        return [];
      });
  }

  const addToReadingList = (id) => {
    axios.post(`${endpoints.reading_list}`, {"article_id": id})
    .then(_ => {
      retrieveReadingList(1);
    })
    .catch(err => {
      console.log(err);
    })
  }

  const removeFromReadingList = (id) => {
    axios.delete(`${endpoints.reading_list}/${id}`)
    .then(_ => {
      retrieveReadingList(1);
    })
    .catch(err => {
      console.log(err);
    })
  }

  const changeDisplay = (type) => {
    setDisplayed(type);
    if (type === "articles") {
      retrieveArticles("", 1);
    } else {
      retrieveReadingList(1);
    }
  };

  const search = (e) => {
    e.preventDefault();
    retrieveArticles(e.target[0].value, 1)
  }

  useEffect(() => {
    retrieveArticles("", 1);
    retrieveReadingList(1);
  }, []);

  return (
    <div className="App">
      <Menu changeDisplay={changeDisplay} />
      <ArticlesList
        searchSubmit={search}
        articles={displayed === "articles" ? articles : readingList}
        showSearch={displayed === "articles"}
        page={page}
        total={totalPages}
        totalRecords={totalRecords}
        changePage={displayed === "articles" ? retrieveArticles : retrieveReadingList}
        term={search_term}
        addToReadingList={addToReadingList}
        removeFromReadingList={removeFromReadingList}
        readingList={readingList}
      />
    </div>
  );
}

export default App;