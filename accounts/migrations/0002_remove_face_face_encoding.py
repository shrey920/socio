# Generated by Django 2.0.3 on 2019-03-30 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='face_encoding',
        ),
    ]
