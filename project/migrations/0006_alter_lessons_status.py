# Generated by Django 4.1.7 on 2023-04-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_lessons_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='status',
            field=models.CharField(choices=[('paye7_season1', 'paye7_season1'), ('paye7_season2', 'paye7_season2')], max_length=50),
        ),
    ]
