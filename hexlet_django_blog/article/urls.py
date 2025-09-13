from django.urls import path
from .views import ArticleIndexView

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="article_list"),
    path("<str:tags>/<int:article_id>/", ArticleIndexView.as_view(), name="article"),
]
