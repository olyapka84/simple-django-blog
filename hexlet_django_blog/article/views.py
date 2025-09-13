from django.views import View
from django.http import HttpResponse


class ArticleIndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
