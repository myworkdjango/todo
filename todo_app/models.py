from django.db import models
import datetime
from django.urls import reverse

class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateTimeField(default=datetime.date.today)

# Create your models here.
