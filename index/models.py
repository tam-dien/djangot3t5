from django.db import models

# Create your models here.

class GroupProduct(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, null=True)