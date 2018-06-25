from django.db import models
from django.utils import timezone


class SmsList(models.Model):
    sender_name = models.TextField()
    message = models.TextField()
    SEVICE_LIST = (
        ('r', 'RouteSMS'),
        ('c', 'CLX'),
    )
    service = models.CharField(max_length=1, choices=SEVICE_LIST, default='r', help_text='Service to send')
    TEXT_TYPES = (
        ('t', 'Text'),
        ('u', 'Unicode'),
    )
    type_text = models.CharField(max_length=1, choices=TEXT_TYPES, default='u', help_text='Format text')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)
    periodic_hour = models.IntegerField(default=0)
    periodic_minutes = models.IntegerField(default=0)
    planned_date = models.DateField(default=0)
    planned_hour = models.IntegerField(default=0)
    planned_minutes = models.IntegerField(default=0)

    def __str__(self):
        return self.sender_name


class SmsTable(models.Model):
    number = models.TextField()
    message = models.TextField()
    smsList = models.ForeignKey('sms.SmsList', on_delete=models.CASCADE)
    date_send = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender_name


class NameTemplate(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MessageTemplate(models.Model):
    name = models.CharField(max_length=20, unique=True)
    text = models.TextField()
    TEXT_TYPES = (
        ('t', 'Text'),
        ('u', 'Unicode'),
    )
    type = models.CharField(max_length=1, choices=TEXT_TYPES, default='u')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

