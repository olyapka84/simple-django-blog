from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        url = reverse("article", kwargs={"tags": "python", "article_id": 42})
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


def about(request):
    return render(request, "about.html")
