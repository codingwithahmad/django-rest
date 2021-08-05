#from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from blog.models import Articles
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ArticleSerializer, UsersSerializer
from django.contrib.auth.models import User

# Create your views here.
class ArticleList(ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


# @api_view(['DELETE', ])
# def delete_article(request, pk):
#     try:
#         article_post = Articles.objects.filter(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "DELETE":
#         operation = article_post.delete()
#         data = {}
#         if operation:
#             data["success"] = "delete successful"
#         else:
#             data["failure"] = "somethings wrong"

#         return Response(data=data)

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailUpdate(RetrieveUpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailDelete(RetrieveDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailSlug(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"







class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer