# Generated by Django 2.0.3 on 2018-03-24 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20180324_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='group',
        ),
    ]
