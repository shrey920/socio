# Generated by Django 2.0.3 on 2018-04-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_file_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='sha1',
            field=models.CharField(default=11111111111111111111, max_length=20),
            preserve_default=False,
        ),
    ]
