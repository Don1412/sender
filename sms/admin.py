from django.contrib import admin
from .models import SmsList, NameTemplate, MessageTemplate

admin.site.register(SmsList)
admin.site.register(NameTemplate)
admin.site.register(MessageTemplate)