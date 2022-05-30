from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.forms import PostForm

from blog.models import Post
# Create your views here.

def home(request):
    return render(request, 'blog/post_list.html')

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostAddView(CreateView):
    model= Post
    form_class= PostForm
    template_name= 'blog/post_create.html' 
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_detail.html'