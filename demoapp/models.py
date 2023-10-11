from django.db import models

# Create your models here.


class task(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    Date = models.DateField(max_length=100)


