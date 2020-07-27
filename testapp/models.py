
# Create your models here.
from django.db import models

class User(models.Model):                           # 一个Model类将对应数据库中的一个表  -- 基类
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    birthday = models.DateTimeField()