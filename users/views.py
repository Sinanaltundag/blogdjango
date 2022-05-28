from django.shortcuts import redirect, render
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import  login, logout
from django.contrib import messages

from users.forms import UserForm
# Create your views here.


def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    # return redirect('logout')
    return render(request, 'users/user_logout.html')


def register(request):
    form_user = UserForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            login(request, user)
            messages.success(request, 'Register Successfull!')
            return redirect('home')
    context = {
        "form_user": form_user,
    }

    return render(request, 'users/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        
        if user:
            messages.success(request, "Login Successfull")
            login(request,user)
            return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})
