from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('name_template/', views.NameTemplateView.as_view(), name='nameTemplate'),
    path('delete_name_template/', views.DeleteNameTemplateView.as_view(), name='deleteNameTemplate'),
    path('message_template/', views.MessageTemplateView.as_view(), name='messageTemplate'),
    path('templates/', views.TemplatesView.as_view(), name='templates'),
    path('create_send/', views.CreateSendView.as_view(), name='createSend')
]
