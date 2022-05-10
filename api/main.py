from fastapi import FastAPI
from app.routers import articles, readling_list

app = FastAPI()
app.include_router(articles.router)
app.include_router(readling_list.router)


@app.get("/health")
def health():
    return "ok"
