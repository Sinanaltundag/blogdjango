
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('slug', 'user')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("content",)