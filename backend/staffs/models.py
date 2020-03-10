from django.db import models

# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.CharField(max_length=255)
    staff_type = models.CharField(max_length=255)
    id = models.AutoField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)

    class Meta:
        unique_together = (("id", "election"))


class IRAROPollingDistricts(models.Model):
    aro = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE)
    polling_district = models.ForeignKey(
        "units.PollingDistricts", on_delete=models.CASCADE)

    class Meta:
        unique_together: (("aro", "polling_district"))
