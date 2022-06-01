from django.contrib import admin

from blog.models import Category, Comment, Like, Post, PostView

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)