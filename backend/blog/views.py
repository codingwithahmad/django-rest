from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView 
from .models import Articles
# Create your views here.

class ArticleList(ListView):
    def get_queryset(self):
        return Articles.objects.filter(status=True)


class ArticleDetail(DetailView):
    def get_object(self):
        primary_key = self.kwargs.get("pk")
        return get_object_or_404(Articles.objects.filter(status=True),
         pk=primary_key
        )