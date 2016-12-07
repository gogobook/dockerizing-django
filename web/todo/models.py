from django.db import models

# Create your models here.

class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateField(auto_now=True)
