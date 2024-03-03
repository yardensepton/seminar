from fastapi import FastAPI
from src.routers import item_route


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    app.include_router(
        item_route.router
    )

    return app
