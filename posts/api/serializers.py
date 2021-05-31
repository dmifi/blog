from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post, Category


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]


class PostSerializers(serializers.ModelSerializer):
    author = AuthorSerializers(many=False, read_only=True)
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author", "category"]


