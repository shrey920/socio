# Generated by Django 2.0.3 on 2019-02-04 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_sosmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sosmessage',
            name='message',
        ),
    ]
