from django.db import models

# Create your models here.

class Login(models.Model):
    trinity_id = models.CharField('',max_length=200)
    trinity_password = models.CharField('',max_length=500)

    objects = models.Manager()