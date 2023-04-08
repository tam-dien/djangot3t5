from django.db import models

# Create your models here.

### ORM objects relational mapping

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()