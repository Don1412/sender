from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('name_template/', views.NameTemplateView.as_view(), name='nameTemplate'),
    path('message_template/', views.MessageTemplateView.as_view(), name='messageTemplate')
]
