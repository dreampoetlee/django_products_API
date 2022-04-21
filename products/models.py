from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class Product(models.Model):
  image = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  inventory_quantity = models.IntegerField()