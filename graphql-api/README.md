# GraphQL API

The purpose of this API is to retrieve the articles information from mongoDB and adding articles to the bookmarks.

## Configuring

### Prerequisites
* Python >=3.7
* virtualenv (recommended)

Execute the following commands to configure the environment (Unix based):
```shell
$ cd articles-challenge/api/
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ make init
```

### Executing tests

To execute all the tests, execute the following command:

```shell
$ make unit
```

### Linting
To follow PEP8 coding stardards, it's possible to verify if everything is correct using `make lint`. This is good to prevent multiple devs working on a project using different standards.

It's possible to verify linting using:
```shell
$ make lint
```

### Environment Variables
* `MONGO_HOST`: The mongodb instance URL. It defaults to `localhost:27017`.

## Starting the API
It's possible to use `docker-compose` to setup the entire environment (please check the documentation on `../`), but if we need to run the API locally (without docker), it's possible to use:

```shell
$ uvicorn main:app --reload
```

## Improvements
* Currently the errors are handled on each endpoint. It would be a better approach to add a middleware to handle all possible errors. If it's based on a known error, we would have the status code and return appropriately if not, a 5XX error would be returned.

* Since `mongoimport` creates an `ObjectId` for each entry, I didn't bother on changing this. If I had more time, I would try making the `cord_uid` as the `ObjectId`.

* Currently it searchs for a certain term on the title. It would be good to improve this to look at the abstract or any other attribute. It currently uses a regex to find it (case insensitive), but this is currently [not the best practice](https://www.mongodb.com/docs/manual/core/index-text/#case-insensitivity). With more time I would have created a separate index for that.