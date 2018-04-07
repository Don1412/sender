from django.db import models
from django.utils import timezone

class list(models.Model):
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
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='none')
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender_name
