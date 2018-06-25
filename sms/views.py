from django import views
from django.contrib.auth import logout, authenticate, login
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import NameTemplate, MessageTemplate, SmsList, SmsTable
from django.http import JsonResponse, HttpResponse
from SMSSender.tasks import add, hi
from django.contrib import messages
import datetime

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
        #add.delay(2, 2)
        #hi.delay()
        return render(request, 'create.html', {'name_template_items': name_template_items,
                                               'message_template_items': message_template_items,
                                               })

    def post(self, request):
        return 1


class NameTemplateView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

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
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('ok')

    def post(self, request):
        NameTemplate.objects.filter(name=request.POST.get('name'), user=self.request.user).delete()
        return HttpResponse('1')


class MessageTemplateView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        template = MessageTemplate.objects.filter(name=request.GET.get('name'), user=self.request.user).first()
        if not template:
            return HttpResponse('Template not found', status=404)
        result = {
            'template': model_to_dict(template)
        }
        return JsonResponse(result)

    def post(self, request):
        message_template = MessageTemplate.objects.create(name=request.POST.get('name'), text=request.POST.get('text'), user=self.request.user)
        message_template.save()
        result = {
            'template': model_to_dict(message_template)
        }
        return JsonResponse(result)


class DeleteMessageTemplateView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('ok')

    def post(self, request):
        MessageTemplate.objects.filter(name=request.POST.get('name'), user=self.request.user).delete()
        return HttpResponse('1')


class TemplatesView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        #name_template_items = NameTemplate.objects.filter(user=self.request.user)
        #message_template_items = MessageTemplate.objects.filter(user=self.request.user)
        return render(request, 'templates.html', {})#'name_template_items': name_template_items,
                                               #'message_template_items': message_template_items})

    def post(self, request):
        return HttpResponse('1')


class CreateSendView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('1')

    def post(self, request):
        service = request.POST.get('selectService')
        sender_name = request.POST.get('senderName')
        numbers = request.POST.get('numbers')
        type = request.POST.get('type')
        message = request.POST.get('message')
        periodic = request.POST.get('periodic')
        if periodic == 'on':
            periodic_hour = int(request.POST.get('periodic_hour'))
            periodic_minutes = int(request.POST.get('periodic_minutes'))
            periodic_amount = int(request.POST.get('periodic_amount'))
        else:
            periodic_hour = 0
            periodic_minutes = 0
            periodic_amount = 1
        planned = request.POST.get('planned')
        if planned == 'on':
            planned_date = request.POST.get('plan_date')
            planned_hour = int(request.POST.get('plan_hour'))
            planned_minutes = int(request.POST.get('plan_minute'))
        else:
            planned_date = 0
            planned_hour = 0
            planned_minutes = 0
        date_send = datetime.date(*[int(j) for j in planned_date.split("-")])
        create_send = SmsList.objects.create(sender_name=sender_name, message=message, type_text=type,
                                             user=self.request.user, service=service, periodic_hour=periodic_hour,
                                             periodic_minutes=periodic_minutes, planned_date=planned_date,
                                             planned_hour=planned_hour, planned_minutes=planned_minutes)
        create_send.save()
        numbers = numbers.split('\n')
        instances = []

        for i in range(0, len(numbers)):
            time_send = datetime.time(hour=planned_hour + periodic_hour * periodic_amount * i,
                                      minute=planned_minutes + periodic_minutes * periodic_amount * i)
            datetime_send = datetime.datetime(
                year=date_send.year,
                month=date_send.month,
                day=date_send.day,
                hour=time_send.hour,
                minute=time_send.minute)
            instances.append(
                SmsTable(number=numbers[i], message=message, smsList=create_send, date_send=datetime_send)
            )

        SmsTable.objects.bulk_create(instances)
        messages.success(request, "К отправке номеров: {}".format(len(numbers)))
        return redirect('create')


class ManagerView(views.View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = False):
        if not id:
            table_items = SmsList.objects.filter(user=self.request.user)
            render_to = 'manager_short.html'
        else:
            table_items = SmsTable.objects.filter(smsList_id=id)
            render_to = 'manager_full.html'
        return render(request, render_to, {'table_items': table_items
                                               })
