from django.shortcuts import render, redirect
from .forms import UserRegistration, ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    page = 'register'
    form = UserRegistration()

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()#so the user will not be key sensitive
            user.save()
            messages.info(request, 'User account was created!')
            #will login the registred user
            #login(request,user)
            #will redirect user at the page it was previously
            return redirect(request.GET['next'] if 'next' in request.GET else 'products')#it's redirected either to the previous page that they were, or(else) to product page
        else:
            messages.error(request, 'An error has occured during registration')
            

    return render(request, 'users/register_login.html', {'page':page, 'form':form})

def loginUser(request):
    page = 'login'

    #if user is already authenticated
    if request.user.is_authenticated:
        return redirect('products')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:#compare usernames from DB with entered data
            user = User.objects.get(username=username)
        except:
            messages.error(request, f'Username {username} does not exist!')
        
        #function will return instance if user exist, and NONE if not
        user = authenticate(request, username=username, password=password)

        if user is not None:#check is user exist
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

@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    return render(request, 'users/account.html', {'profile':profile})

@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('account')

    return render(request, 'users/edit_account.html', {'form':form})