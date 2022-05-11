# Articles FE

## Configuring

### Prerequisites
* nodejs
* npm

#### Environment Variables
* `REACT_APP_API_URL`: URL for the API (usually `localhost:8000`)

### Getting Started
As soon as you load the page, 10 articles will show up. It's also possible to see next ones clicking on the pages. If you want to search for a certain term on the title, use the search bar and press enter when you want to submit.

There are two icons at the bottom of each article. It's possible to view it or add it to the reading list. In case you want to remove it from the list, just click on the icon again.

Execute the following commands to configure the environment (Unix based):
```shell
$ cd articles-challenge/fe/
$ npm install
$ export REACT_APP_API_URL=http://localhost:8000 && npm start
```

> Recommendation: use `docker-compose` (check `../README.md` for more information).

### Improvements
* Currently in case of any API errors, the error is logged to the console. It would be better to have a proper toast showing the error information.

### Known Issues
* When moving further than the fifth page (considering there is more), the ellipsis is shown before the active page.