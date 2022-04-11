from app.endpoints import change_user_status_endpoint, create_user_endpoint, get_one_user_endpoint, update_user_endpoint
from dotenv import load_dotenv
from fastapi import FastAPI
from . import get_users_endpoint


load_dotenv()


def create_app():
    app = FastAPI()
    app.include_router(get_users_endpoint.router)
    app.include_router(create_user_endpoint.router)
    # app.include_router(get_one_user_endpoint.router)
    # app.include_router(update_user_endpoint.router)
    # app.include_router(change_user_status_endpoint.router)
    return app
