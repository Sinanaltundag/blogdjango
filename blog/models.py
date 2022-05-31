import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to="blog_pics", default='blog_pics/default.png')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES=(
        ("1",'published'), 
        ("2",'draft'), 
        ("3",'pending')
        )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)+str(uuid.uuid4())
        return super().save(*args, **kwargs)

    def get_comment_count(self):
        comments = self.comment_set.all()
        return comments.count()

class Comment(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Like(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class PostView(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
