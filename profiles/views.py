from django.shortcuts import render, redirect, HttpResponse
from .models import UserProfile
from .forms import UpdateProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Create your views here.
def profile(request, pk):
    user_profile = UserProfile.objects.get(profile_id=pk)
    context = {'profile': user_profile}
    return render(request, 'profiles_app/profile.html', context)


def account(request):
    user_account = request.user.userprofile
    context = {
        'account': user_account
    }
    return render(request, 'profiles_app/account.html', context)


def UpdateProfile(request, pk):
    profile = request.user.userprofile
    obj = UserProfile.objects.get(profile_id=pk)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=obj, initial={'username': profile.username})
        if form.is_valid():
            form.save()
            messages.info(request, 'Your Profile looks Good!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'profiles_app/updateProfile.html', context)


def DeleteProfile(request):
    profile = request.user.userprofile
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        user = request.user
        user.delete()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profiles_app/deleteProfile.html', context)


def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your Account has been created, Login to start')
            return redirect('login_user')

    return render(request, 'profiles_app/register.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome Back ' + username)
            return redirect('index')

        else:
            messages.info(request, 'username OR password is incorrect')

    return render(request, 'profiles_app/login.html', {})


def logoutUser(request):
    logout(request)
    messages.info(request, 'logged out')
    return redirect('login_user')
