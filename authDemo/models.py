from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    pwd = models.CharField(max_length=32,verbose_name='密码')
    token = models.UUIDField()
