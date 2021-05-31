from rest_framework import generics
from posts.models import Post
from .serializers import PostSerializers


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


