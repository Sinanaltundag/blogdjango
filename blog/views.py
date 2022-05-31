from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.forms import CommentForm, PostForm

from blog.models import Comment, Post, PostView
# Create your views here.

def home(request):
    return render(request, 'blog/post_list.html')

class PostListView(ListView):
    model = Post

        


# class PostDetailView(DetailView):
#     model = Post
#     form_class= CommentForm
#     template_name = "blog/post_detail.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         print(self)
#         return super().form_valid(form)




def detailView(request, slug):
    post =  get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')
    print(len(comments))
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None )
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        comment_form = CommentForm()
    context = {'post': post,
           'comments': comments,
           'comment_form' : comment_form,
           }
    return render(request, 'blog/post_detail.html', context)


class PostAddView(CreateView):
    model= Post
    form_class= PostForm
    template_name= 'blog/post_create.html' 
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model= Post
    form_class= PostForm
    template_name= 'blog/post_update.html'
    success_url = reverse_lazy("home")

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'blog/post_detail.html'