from django.contrib import admin

# Register your models here.
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "time_of_publication", "created", "updated", "status", "category",)


# admin.site.register(Post)
admin.site.register(Category)

