from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.forms import CommentForm, PostForm
from blog.models import Comment, Like, Post, PostView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

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
        if request.user.is_authenticated:
            PostView.objects.get_or_create(user=request.user, post=post) # for calculate single view count, add new row Postview
 
    context = {'post': post,
           'comments': comments,
           'comment_form' : comment_form,
           }
    return render(request, 'blog/post_detail.html', context)



def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    Like.objects.get_or_create(user=request.user, post=post)
    return HttpResponseRedirect(reverse('post_detail', args=[str(post.slug)]))


class PostAddView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model= Post
    form_class= PostForm
    template_name= 'blog/post_create.html' 
    success_url = reverse_lazy("home")
    @property
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