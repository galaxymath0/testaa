# Generated by Django 4.1.7 on 2023-04-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_lessons_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='status',
            field=models.CharField(choices=[('paye7_season1', 'paye7_season1'), ('paye7_season2', 'paye7_season2'), ('paye7_season3', 'paye7_season3'), ('paye7_season4', 'paye7_season4'), ('paye7_season5', 'paye7_season5'), ('paye7_season6', 'paye7_season6'), ('paye7_season7', 'paye7_season7'), ('paye7_season8', 'paye7_season8'), ('paye7_season9', 'paye7_season9')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
