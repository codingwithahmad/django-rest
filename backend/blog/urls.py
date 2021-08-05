from django.urls import path
from . import views
#urls here
app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="home"),
    path('<int:pk>', views.ArticleDetail.as_view(), name="detail"),
]