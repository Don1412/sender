from django import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm, LoginForm


class RegisterView(views.View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'Register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return render(request, 'Register.html', {'form': form})


class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            return redirect(reverse('index'))
        return render(request, 'Login.html', {'form': form})


class IndexView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'index.html', {})
