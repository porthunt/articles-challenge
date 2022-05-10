import os

MONGODB_INFO = {
    "username": os.getenv("MONGO_USERNAME", ""),
    "password": os.getenv("MONGO_PWD", ""),
    "host": os.getenv("MONGO_HOST", "localhost"),
    "port": int(os.getenv("MONGO_PORT", 27017)),
    "db_name": "healx-challenge",
    "timeout": 5000,
}
