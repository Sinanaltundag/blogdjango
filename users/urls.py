
from django.urls import path

from users.views import register, user_login, user_logout, profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='users/change-password.html'), name="change-password"),
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='users/reset-password.html'), name="reset-password"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/reset_password_sent.html'), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/change-password.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/reset_password_sucess.html'), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
