# Generated by Django 2.0.3 on 2019-02-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_file_sha1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='message/uploads/'),
        ),
    ]
