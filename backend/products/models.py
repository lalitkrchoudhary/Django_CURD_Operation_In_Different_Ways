from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

