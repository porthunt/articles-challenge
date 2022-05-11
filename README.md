# articles-challenge
The purpose of this challenge is to create an API (`api/`) that retrieves articles data and also allow adding items to a reading list. This data needs to be available for the frontend (`fe/`) to consume and display it.

For more information on each specific part of the code, please access their directories.

## Building

It is possible to use `docker-compose` to setup the entire environment. It will create 4 containers:
* `mongo`: deploys a mongodb locally (running on a different port, don't worry if you have one setup already).
* `load-mongo`: downloads the CSV file from S3 and imports it to `mongo`. It shuts down once its done.
* `api`: deploys the API locally to port `8080`.
* `fe`: deploys the frontend locally to port `3000`.

To start the services, type:
```shell
$ cd articles-challenge/
$ docker-compose build --no-cache
$ docker-compose up
```

> Note: It might take a couple of seconds for `load-mongo` to import everything. It will depend on your internet speed to download the csv file.

This will not run on dettach mode, so when you don't need the services anymore, you can press `Ctrl+C` or `Cmd+C`, which will stop the containers.

You can execute `docker-compose rm` to remove them.