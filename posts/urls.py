from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path("post/create/", PostCreateView.as_view()),
    path("post/list/", PostListView.as_view()),
    path("post/list/<int:pk>", PostDetailView.as_view()),
]


