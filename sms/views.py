from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

class RegisterView:
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "../../SMSSender/templates/Register.html"

    def register(request):
        if request.method == 'POST':
            form = RegisterForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('../login/')
        else:
            form = RegisterForm()
        return render(request, 'Register.html', {'form': form})

class LoginView:
    form_class = AuthenticationForm
    success_url = "/sms/"
    template_name = "../../SMSSender/templates/Login.html"

    def login(request):
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            print(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                form.save()
                return redirect('../sms/')
        else:
            form = LoginForm()
        print('lol')
        return render(request, 'Login.html', {'form': form})
