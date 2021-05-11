from django.db import models

# Create your models here.

class human(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    Over18 = models.BooleanField(default=False)
    