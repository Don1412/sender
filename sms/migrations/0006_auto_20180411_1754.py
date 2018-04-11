# Generated by Django 2.0.4 on 2018-04-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20180410_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='smslist',
            name='sms_key',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='nametemplate',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
