from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username','email')
class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
