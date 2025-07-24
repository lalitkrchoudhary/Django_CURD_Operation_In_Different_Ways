from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname= models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


    