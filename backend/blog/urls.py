from django.urls import path
from . import views
#urls here
app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="home"),
    path('<int:pk>', views.ArticleDetail.as_view(), name="detail"),
    path('<slug:slug>', views.ArticleDetailSlug.as_view(), name="articles_slug"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail")
]