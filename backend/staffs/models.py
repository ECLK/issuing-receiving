from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Staffs(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.CharField(max_length=255, unique=True)

class IRARO(models.Model):
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE, related_name="aros")
    election = models.ForeignKey("election.Election", on_delete=models.CASCADE, related_name="aros")
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="aro")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["staff", "election"], name="Staff_election")]
        

class IRAROPollingDistricts(models.Model):
    aro = models.ForeignKey(IRARO, on_delete=models.CASCADE, related_name="polling_districts")
    polling_district = models.ForeignKey(
        "units.PollingDistrict", on_delete=models.CASCADE, related_name="IRAROs")

    class Meta:
        constraints=[models.UniqueConstraint(fields=["aro","polling_district"], name="aro_pd")]



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
