from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username','email')
class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

# image resizer with pillow 
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path) 

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)
