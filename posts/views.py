from rest_framework import generics
from .serializers import PostSerializers
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )


