
from django.contrib import messages
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


def detailView(request, slug):
    # Post modelinden slugları eşit olanı getir
    post = get_object_or_404(Post, slug=slug)
    # posta ait commentleri getir ve ters sırala
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        # post ise formu doldur
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            # formun bir kısmını otomatik doldurma yöntemi, önce formu db'ye göndermeden kaydet, istediklerini ekle ve db'ye gönder
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        comment_form = CommentForm()
        if request.user.is_authenticated:
            # for calculate single view count, add new row Postview
            PostView.objects.get_or_create(user=request.user, post=post)

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)

#  post id sinde alıp Like modeline user ve post isimlerini kaydediyoruz, HttpResponseRedirect ile aynı sayfada kalmasını sağlayabiliriz
def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if request.user.is_authenticated:
        Like.objects.get_or_create(user=request.user, post=post)
        return HttpResponseRedirect(reverse('post_detail', args=[str(post.slug)]))
    else:
        messages.success(request, 'You need to login first to like this post')
        return HttpResponseRedirect(reverse('post_detail', args=[str(post.slug)]))


class PostAddView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("home")
# form valid fonksiyonunu override ederek formun instance'ına aktif user'ı ekliyoruz
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy("home")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    # aynı sayfada silme işlemi için
    template_name = 'blog/post_detail.html'
