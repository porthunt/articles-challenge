from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import schema
from strawberry.asgi import GraphQL


graphql_app = GraphQL(schema)

app = FastAPI(
    title="Articles API - GraphQL",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_route("/", graphql_app)
