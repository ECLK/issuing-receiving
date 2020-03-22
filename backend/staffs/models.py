from django.db import models

# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.CharField(max_length=255, unique=True)


class IRAROPollingDistricts(models.Model):
    aro = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE, related_name="IRAROs")
    polling_district = models.ForeignKey(
        "units.PollingDistrict", on_delete=models.CASCADE, related_name="IRAROs")
    election = models.ForeignKey(
        "election.Election", on_delete=models.CASCADE, related_name="IRAROs")

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["polling_district", "election"], name="pd_election"),]


class PDStorageInCharge(models.Model):
    in_charge = models.ForeignKey(
        "staffs.Staffs", on_delete=models.CASCADE, related_name="storage_in_charges")
    polling_division = models.ForeignKey(
        "units.PollingDivision", on_delete=models.CASCADE, related_name="storage_in_charges")
    election = models.ForeignKey(
        "election.Election", on_delete=models.CASCADE, related_name="storage_in_charges")

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["polling_division", "election"], name="storage_pd_election"),
            models.UniqueConstraint(fields=["in_charge","election"], name="in_charge_election")]
