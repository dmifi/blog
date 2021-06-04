from rest_framework import generics
from .serializers import PostSerializers
from .models import Post


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()


