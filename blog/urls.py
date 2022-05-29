from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostAddView, PostDetailView, PostListView

urlpatterns = [
    path("<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
    path('add/', PostAddView.as_view(), name="add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
