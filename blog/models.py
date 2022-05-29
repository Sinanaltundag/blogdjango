from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to="blog_pics", blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class PostView(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
