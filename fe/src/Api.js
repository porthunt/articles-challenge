const BASE_URL = process.env.REACT_APP_API_URL

const endpoints = {
    get_articles: BASE_URL + "/articles",
    reading_list: BASE_URL + "/reading-list"
}

export { endpoints };