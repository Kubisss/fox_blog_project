from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'created_at', 'updated_at', 'content', 'author']
