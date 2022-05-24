from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField()
    location = models.CharField(max_length=50,null=True,blank=True)
