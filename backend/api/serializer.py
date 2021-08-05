from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        # fields = (
        #     "title", 
        #     "slug", 
        #     "content", 
        #     "author", 
        #     "publish",  
        #     "status"
        # )
        exclude = ('created', 'updated')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
     