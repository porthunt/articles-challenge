# GraphQL API

Query
```
{
  articles(page: 1, limit: 4) {
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
```