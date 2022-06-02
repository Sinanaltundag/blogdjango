from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

# üstteki modelde password inputu çağırılmadan gelir, alttaki bizim oluşturduğumuz form ve password gelmez


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        # Formda görülmesini istediğiniz label burada değişir
        labels = {
            "profile_pic": "Profile Picture",
            "bio": "Biography",
        }
