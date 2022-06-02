from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostAddView, PostDeleteView, PostUpdateView, detailView, likeView

urlpatterns = [
    path("<slug:slug>", detailView, name="post_detail"),
    path('add/', PostAddView.as_view(), name="post_add"),
    path('post_update/<int:pk>', PostUpdateView.as_view(), name="post_update"),
    path('post_delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
    path('post_like/<int:pk>', likeView, name="post_like"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static ve media dosyalarını almak ve görüntülemek için üst satır eklenir