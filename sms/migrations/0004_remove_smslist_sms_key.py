# Generated by Django 2.0.4 on 2018-06-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_remove_smstable_sms_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smslist',
            name='sms_key',
        ),
    ]
