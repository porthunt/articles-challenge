# GraphQL API

Query
```
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

{"page": 1, "limit": 4, "term": "Brazil"}
```

Query Bookmarks
```
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
```

Add Bookmarks
```
mutation AddBookmark($articleId: String!) {
  addBookmark(articleId: $articleId) {
  	title
  }
}

{"articleId": "629c9003246297b851beddc7"}
```