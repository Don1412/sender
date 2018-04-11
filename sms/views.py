from django import views
from django.contrib.auth import logout, authenticate, login
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import NameTemplate, MessageTemplate
from django.http import JsonResponse, HttpResponse

from .forms import RegisterForm, LoginForm


class RegisterView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

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
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))
        return render(request, 'Login.html', {'form': form})


class IndexView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'index.html', {})


class LogoutView(views.View):
    def get(self, request):
        if self.request.user.is_authenticated:
            logout(request)
            return redirect(reverse('login'))
        return render(request, 'index.html', {})


class CreateView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        name_template_items = NameTemplate.objects.filter(user=self.request.user)
        message_template_items = MessageTemplate.objects.filter(user=self.request.user)
        return render(request, 'create.html', {'name_template_items': name_template_items,
                                               'message_template_items': message_template_items})

    def post(self, request):
        return 1


class NameTemplateView(views.View):
    def get(self, request):
        template = NameTemplate.objects.filter(name=request.GET.get('name'), user=self.request.user).first()
        if not template:
            return HttpResponse('Template not found', status=404)
        data = {'template': model_to_dict(template)}
        return JsonResponse(data)

    def post(self, request):
        name_template = NameTemplate.objects.create(name=request.POST.get('name'), user=self.request.user)
        name_template.save()
        result = {
            'template': model_to_dict(name_template)
        }
        return JsonResponse(result)


class DeleteNameTemplateView(views.View):
    def get(self, request):
        return HttpResponse('ok')

    def post(self, request):
        NameTemplate.objects.filter(name=request.POST.get('name'), user=self.request.user).delete()
        return HttpResponse('1')


class MessageTemplateView(views.View):
    def get(self, request):
        template = MessageTemplate.objects.filter(name=request.GET.get('name'), user=self.request.user).first()
        if not template:
            return HttpResponse('Template not found', status=404)
        result = {
            'template': model_to_dict(template)
        }
        return JsonResponse(result)

    def post(self, request):
        name_template = NameTemplate.objects.create(name=request.POST.get('name'), user=self.request.user)
        name_template.save()
        result = {
            'template': model_to_dict(name_template)
        }
        return JsonResponse(result)
