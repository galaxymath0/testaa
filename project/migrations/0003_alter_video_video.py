# Generated by Django 4.1.7 on 2023-04-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/'),
        ),
    ]
