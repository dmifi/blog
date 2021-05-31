from django.urls import path
from .views import PostsListView, json_list_published_posts

app_name = 'posts'

urlpatterns = [
    path('', PostsListView.as_view()),
    # path('api/posts/', json_list_published_posts),
]


