from django.urls import path

from users.views import user_login


urlpatterns = [
path("login/", user_login, "user_login.html")

]
