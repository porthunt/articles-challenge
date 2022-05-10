from fastapi import HTTPException


class Error(Exception):
    default_message = ""

    def __init__(self, message=None, **kwargs):
        Exception.__init__(self)
        self.message = (
            message if message else self.default_message.format(**kwargs)
        )

    def http_exception(self):
        return HTTPException(status_code=self.status_code, detail=self.message)


class ArticleNotFoundError(Error):
    status_code = 404
    default_message = "The Article ID was not found"


class ReadListItemConflictError(Error):
    status_code = 409
    default_message = "Article is already on the Reading List"


class InvalidArticleIDError(Error):
    status_code = 400
    default_message = "The Article ID is not a valid ID"


class UnknownError(Error):
    status_code = 500
    default_message = "Unknown error"


class DBUnreachableError(Error):
    status_code = 503
    default_message = "Can't reach MongoDB"
