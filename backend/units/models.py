from django.db import models

# Create your models here.
STAFF_MODEL = "staffs.Staffs"


class ElectoralDistricts(models.Model):
    name = models.CharField(max_length=100)


class AdministrativeDistricts(models.Model):
    name = models.CharField(max_length=100)
    electoral_district = models.ForeignKey(
        'ElectoralDistricts', on_delete=models.SET_NULL)


class PollingDivisions(models.Model):
    name = models.CharField(max_length=100)
    administrative_district = models.ForeignKey(
        'AdministrativeDistricts', on_delete=models.SET_NULL)


class PollingDistricts(models.Model):
    name = models.CharField(max_length=100)
    polling_division = models.ForeignKey(
        'PollingDivisions', on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey(STAFF_MODEL, on_delete=models.SET_NULL)


class PollingStations(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(unique=True)
    spo = models.ForeignKey(STAFF_MODEL, on_delete=models.SET_NULL)


class CountingCentre(models.Model):
    name = models.CharField(max_field=255)
    number = models.IntegerField(unique=True)
    cco = models.ForeignKey(STAFF_MODEL, on_delete=models.SET_NULL)
