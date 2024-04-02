from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, EditUserForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))

def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form=SignUpForm()
            return render(request, 'register_user.html', {'form': form})
        return render(request, 'register_user.html', {'form': form})

def edit_user(request):
    if request.user.is_authenticated:
        form = EditUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                request.user.username = form.cleaned_data['username']
                request.user.email = form.cleaned_data['email']
                request.user.first_name = form.cleaned_data['first_name']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.save()
                return redirect('home')
        return render(request, 'edit_user.html', {'form': form})
    else:
        return redirect('home')

def delete_user(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')

def item_select(request):
    return render(request, 'item_select.html',{})

