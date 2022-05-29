from django.contrib import admin

from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Post, PostAdmin)