# Generated by Django 2.0.3 on 2018-03-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180316_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
