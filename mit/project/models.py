from django.db import models
from enum import unique


# Create your models here.
class  Project(models.Model):
    time = models.DateField()
    title = models.CharField(max_length=128, unique=True)
    company = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title