from django.db import models

# Create your models here.
from django.contrib.postgres.fields import JSONField

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(null=True, blank = True)
    category = models.ForeignKey(Category)
    price = models.IntegerField()
    attributes = JSONField()

    def __str__(self):
        return self.name