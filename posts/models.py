from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
User = get_user_model()


class Category(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='time_of_publication')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    time_of_publication = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, related_name="posts", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
