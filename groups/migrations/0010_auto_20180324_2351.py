# Generated by Django 2.0.3 on 2018-03-24 23:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0009_auto_20180324_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ManyToManyField(related_name='group_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
