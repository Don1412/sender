from django.contrib import admin
from .models import list, name_template, message_template

admin.site.register(list)
admin.site.register(name_template)
admin.site.register(message_template)