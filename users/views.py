from django.shortcuts import render, redirect
from .forms import UserRegistration, ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

# Create your views here.
def register(request):
    page = 'register'
    
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid:
            form.save()
            return redirect('products')
    else:
        form = UserRegistration()
    return render(request, 'users/register_login.html', {'page':page, 'form':form})

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('products')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'Username {username} does not exist!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'{username} successfully logged!')
            return redirect (request.GET['next'] if 'next' in request.GET else 'products')
        else:
            messages.error(request, 'Username or password does not exist!')
    
    return render(request, 'users/register_login.html', {'page':page})


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'User logout!')
        return redirect('products')
    return render(request, 'users/logout.html')


def account(request):
    profile = request.user.profile
    return render(request, 'users/account.html', {'profile':profile})

def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('account')

    return render(request, 'users/edit_account.html', {'form':form})