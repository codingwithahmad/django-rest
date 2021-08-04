from django.urls import path
from . import views
#urls here
app_name = "api"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="home"),
    path('delete/<int:pk>', views.delete_article, name="delete")
]