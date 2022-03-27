from dotenv import load_dotenv
from fastapi import FastAPI
from . import get_users_endpoint


load_dotenv()


def create_app():
    app = FastAPI()
    app.include_router(get_users_endpoint.router)
    return app
