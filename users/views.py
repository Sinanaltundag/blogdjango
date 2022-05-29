from django.shortcuts import redirect, render
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import  login, logout
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm

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

# def user_profile(request):
#     form_profile = UserProfileForm(request.POST, request.FILES)
#     if form_profile.is_valid():
#         profile = form_profile.save(commit=False)
#         print(request.user.id)
#         profile.user = request.user
#         # profile.save()
#         # messages.success(request, 'Update Successful!')
#         # return redirect('home')
    
#     context = {
#         "form_profile": form_profile
#     }

#     return render(request, 'users/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect("home")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})