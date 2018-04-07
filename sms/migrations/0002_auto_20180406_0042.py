# Generated by Django 2.0.4 on 2018-04-05 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='type',
        ),
        migrations.AddField(
            model_name='list',
            name='service',
            field=models.CharField(choices=[('r', 'RouteSMS'), ('c', 'CLX')], default='r', help_text='Service to send', max_length=1),
        ),
        migrations.AddField(
            model_name='list',
            name='type_text',
            field=models.CharField(choices=[('t', 'Text'), ('u', 'Unicode')], default='u', help_text='Format text', max_length=1),
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
