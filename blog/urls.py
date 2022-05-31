from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostAddView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, detailView

urlpatterns = [
    # path("<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>", detailView, name="post_detail"),
    # path("", PostListView.as_view(), name="post_list"),
    path('add/', PostAddView.as_view(), name="post_add"),
    path('post-update/<int:pk>', PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
