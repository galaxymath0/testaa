from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.email
class Lessons(models.Model):
    STATUS_CHOICES = (
        # paye7
        ('paye7_season1' , 'paye7_season1'),
        ('paye7_season2' , 'paye7_season2'),
        ('paye7_season3' , 'paye7_season3'),
        ('paye7_season4' , 'paye7_season4'),
        ('paye7_season5' , 'paye7_season5'),
        ('paye7_season6' , 'paye7_season6'),
        ('paye7_season7' , 'paye7_season7'),
        ('paye7_season8' , 'paye7_season8'),
        ('paye7_season9' , 'paye7_season9'),
        # paye8
        ('paye8_season1' , 'paye8_season1'),
        ('paye8_season2' , 'paye8_season2'),
        ('paye8_season3' , 'paye8_season3'),
        ('paye8_season4' , 'paye8_season4'),
        ('paye8_season5' , 'paye8_season5'),
        ('paye8_season6' , 'paye8_season6'),
        ('paye8_season7' , 'paye8_season7'),
        ('paye8_season8' , 'paye8_season8'),
        ('paye8_season9' , 'paye8_season9'),
        # paye9
        ('paye9_season1' , 'paye9_season1'),
        ('paye9_season2' , 'paye9_season2'),
        ('paye9_season3' , 'paye9_season3'),
        ('paye9_season4' , 'paye9_season4'),
        ('paye9_season5' , 'paye9_season5'),
        ('paye9_season6' , 'paye9_season6'),
        ('paye9_season7' , 'paye9_season7'),
        ('paye9_season8' , 'paye9_season8'),

    )
    title = models.CharField(max_length=100)
    paye = models.CharField(max_length=50)
    lesson = models.CharField(max_length=50)
    video = models.FileField(upload_to='video/%y')
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES)
    def __str__(self):
        return self.slug

     

