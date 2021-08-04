from django.urls import path
from . import views
#urls here
app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="home"),
]