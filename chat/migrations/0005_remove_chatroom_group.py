# Generated by Django 2.0.3 on 2018-03-24 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chatroom_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='group',
        ),
    ]
