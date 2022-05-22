from app.services import ArticleService
from typing import List
from app.models import Article


class AllArticleGetter:
    def __init__(self):
        pass

    def run(self) -> List[Article]:
        articles = []
        article_service = ArticleService()
        articles = article_service.get_all_articles()
        return articles