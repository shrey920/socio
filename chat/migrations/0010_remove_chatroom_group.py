# Generated by Django 2.0.3 on 2018-03-24 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_chatroom_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='group',
        ),
    ]
