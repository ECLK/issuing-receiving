from django.db import models

# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.CharField(max_length=255, unique=True)


class IRAROPollingDistricts(models.Model):
    aro = models.OneToOneField("staffs.Staffs", on_delete=models.CASCADE)
    polling_district = models.ForeignKey(
        "units.PollingDistricts", on_delete=models.CASCADE)
    election = models.ForeignKey("election.Election", on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["polling_district", "election"], name="pd_election")]


class PDStorageInCharge(models.Model):
    in_charge = models.OneToOneField(
        "staffs.Staffs", on_delete=models.CASCADE)
    polling_district = models.ForeignKey(
        "units.PollingDistricts", on_delete=models.CASCADE)
    election = models.ForeignKey("election.Election", on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["polling_district", "election"], name="pd_election")]
