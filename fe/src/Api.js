const API_ENDPOINT = process.env.REACT_APP_API_URL;

const QUERIES = {
    articles: `
      query Info(
        $page: Int
        $limit: Int
        $term: String
      )
      {
        articles(page: $page, limit: $limit, title: $term) {
          pageInfo {
            page
            limit
            totalRecords
            totalPages
          }
          data {
            Id
            title
            journal
            authors
            url
            publishTime
          }
        }
      }
    `,
    bookmarks: `
      {
        bookmarks {
          pageInfo {
            totalRecords
          }
          data {
            Id
            title
            journal
            authors
            url
            publishTime
          }
        }
      }
    `,
    addBookmark: `
      mutation AddBookmark($articleId: String!) {
        addBookmark(articleId: $articleId) {
            title
        }
      }
    `,
    removeBookmark: `
      mutation RemoveBookmark($articleId: String!) {
        removeBookmark(articleId: $articleId) {
            title
        }
      }
    `
};

export { API_ENDPOINT, QUERIES };
