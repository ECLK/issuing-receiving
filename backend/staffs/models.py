from django.db import models

# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.CharField(max_length=255)
    staff_type = models.CharField(max_length=255)
