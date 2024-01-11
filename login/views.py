from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import Petugas

from django.views.generic import (CreateView, UpdateView, DeleteView, ListView)

# Create your views here.
# def = function
def index(request):
    # posts = Post.object.all()

    context = {
        "title":"Login Simparis Hotel",
        # "posts":posts
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                #IF PETUGAS & ADMIN
                return redirect('/dashboard/')
            else:
                # Handle invalid login credentials
                messages.success(request, "Invalid Credentials")
                return redirect('/login/')
    else:
        form = LoginForm()

    return render(request, 'login/index.html', context)

def logoutView(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Sign Out Successful")        
        return redirect('/login/')