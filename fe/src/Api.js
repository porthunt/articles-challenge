const BASE_URL = process.env.REACT_APP_API_URL;

const endpoints = {
  getArticles: BASE_URL + "/articles",
  readingList: BASE_URL + "/reading-list",
};

export { endpoints };
