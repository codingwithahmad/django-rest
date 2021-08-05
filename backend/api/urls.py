from django.urls import path
from . import views
#urls here
app_name = "api"
urlpatterns = [
    path('', views.ArticleList.as_view(), name="home"),
    # path('delete/<int:pk>', views.delete_article, name="delete"),
    path('<int:pk>', views.ArticleDetail.as_view(), name="detail"),
    path('<int:pk>/update', views.ArticleDetailUpdate.as_view(), name="detail_update"),
    path('<int:pk>/delete', views.ArticleDetailDelete.as_view(), name="detail_delete"),


    path('users/', views.UserList.as_view(), name="users"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('<slug:slug>', views.ArticleDetailSlug.as_view(), name="article_slug_view")
]