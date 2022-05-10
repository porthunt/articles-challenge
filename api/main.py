from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import articles, readling_list

app = FastAPI(
    title="Articles API",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles.router)
app.include_router(readling_list.router)


@app.get("/health")
def health():
    return "ok"
