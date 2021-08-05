from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView 
from .models import Articles
from django.contrib.auth.models import User
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

class ArticleDetailSlug(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Articles.objects.filter(status=True), slug=slug)

class UserList(ListView):
    def get_queryset(self):
        return User.objects.all()

class UserDetail(DetailView):
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(User, id=pk)