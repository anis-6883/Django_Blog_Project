from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import (
    UserRegisterForm, 
    UserProfileChangeForm, 
    ChangeProfilePicForm
    )
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account successfully created for {username}')
        return redirect('App_Login:blog-login')
    context = {
        'form' : form
    }
    return render(request, 'App_Login/register.html', context)

def login_page(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             messages.success(request, f'{username} Login Successfully')
             return redirect('App_Blog:blog-home')
    context = {
        'form' : form
    }
    return render(request, 'App_Login/login.html', context)


@login_required
def logout_page(request):
    messages.success(request, f'{request.user.username} Logout Successfully. Log In Again...')
    logout(request)
    return redirect('App_Login:blog-login')


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html')

@login_required
def change_password(request):
    current_user = request.user
    form = PasswordChangeForm(current_user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Password Have Changed...✅ Login Again")
        return redirect('App_Login:blog-profile')

    context = {
        'form' : form
    }
    return render(request, 'App_Login/change_password.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserProfileChangeForm(request.POST, instance=request.user)
        p_form = ChangeProfilePicForm(request.POST, 
        request.FILES,
        instance=request.user.user_profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has Updated...✅')
            return redirect('App_Login:blog-profile')
    else:
        u_form = UserProfileChangeForm(instance=request.user)
        p_form = ChangeProfilePicForm(instance=request.user.user_profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'App_Login/change_profile.html', context)





