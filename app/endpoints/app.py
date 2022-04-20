#Users tag
from app.endpoints import activate_user_endpoint
from app.endpoints import change_user_status_endpoint
from app.endpoints import create_user_endpoint
from app.endpoints import delete_user_endpoint
from app.endpoints import get_all_users_endpoints
from app.endpoints import get_one_user_endpoint
from app.endpoints import update_user_endpoint
from app.endpoints import get_all_users_simple_endpoint

#Articles tag
from app.endpoints import get_all_articles_endpoint
from app.endpoints import create_article_endpoint
from app.endpoints import get_one_user_articles_endpoint
from app.endpoints import get_active_users_articles_endpoint
from app.endpoints import update_articles_endpoint

#Both tag
from app.endpoints import get_all_users_articles_endpoint


from dotenv import load_dotenv
from fastapi import FastAPI
from . import get_users_endpoint


load_dotenv()


def create_app():
    app = FastAPI()
    app.include_router(get_all_users_endpoints.router)
    app.include_router(get_users_endpoint.router)
    app.include_router(create_user_endpoint.router)
    app.include_router(get_one_user_endpoint.router)
    app.include_router(update_user_endpoint.router)
    app.include_router(change_user_status_endpoint.router)
    app.include_router(delete_user_endpoint.router)
    app.include_router(activate_user_endpoint.router)
    app.include_router(get_all_articles_endpoint.router)
    app.include_router(create_article_endpoint.router)
    app.include_router(get_one_user_articles_endpoint.router)
    app.include_router(get_active_users_articles_endpoint.router)
    app.include_router(update_articles_endpoint.router)
    app.include_router(get_all_users_articles_endpoint.router)
    app.include_router(get_all_users_simple_endpoint.router)
    return app
