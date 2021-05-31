from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post, Category
from django.http import JsonResponse


class PostsListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    template_name = 'posts/list.html'


def json_list_published_posts(request):
    posts = Post.objects.filter(status='published')

    return JsonResponse(
        {
            "posts": [
                {
                    "title": p.title,
                    "slug": p.slug,
                    "id": p.id,
                    "published": p.time_of_publication,
                }
                for p in posts
            ]
        }
    )
