from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Category
User = get_user_model()


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]


class PostSerializers(serializers.ModelSerializer):
    # author = AuthorSerializers(many=False, read_only=True)
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault)
    category = CategorySerializers
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["id", "title", 'body', "author", 'status', "category"]


