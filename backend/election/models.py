from django.db import models

# Create your models here.


class Election(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
