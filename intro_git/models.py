from django.db import models

# Create your models here.

class Intro(models.Model):
    username = models.CharField(max_length=120)
    link_git = models.CharField(max_length=256)
    content = models.TextField()
