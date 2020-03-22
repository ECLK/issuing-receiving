from django.db import models

# Create your models here.
STAFF_MODEL = "staffs.Staffs"


class ElectoralDistrict(models.Model):
    name = models.CharField(max_length=100)


class AdministrativeDistrict(models.Model):
    name = models.CharField(max_length=100)
    electoral_district = models.ForeignKey(
        'ElectoralDistrict', on_delete=models.SET_NULL, null=True, related_name="administrative_districts")


class PollingDivision(models.Model):
    name = models.CharField(max_length=100)
    administrative_district = models.ForeignKey(
        'AdministrativeDistrict', on_delete=models.SET_NULL, null=True, related_name="polling_divisions")


class PollingDistrict(models.Model):
    name = models.CharField(max_length=100)
    polling_division = models.ForeignKey(
        'PollingDivision', on_delete=models.SET_NULL, null=True, related_name="polling_districts")


class PollingStation(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    spo = models.ManyToManyField(STAFF_MODEL, related_name="polling_stations")
    election = models.ManyToManyField(
        "election.Election", related_name="polling_stations")
    polling_district = models.ForeignKey(
        PollingDistrict, on_delete=models.CASCADE, related_name="polling_stations")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election", "number"], name="election_number"),
            models.UniqueConstraint(
                fields=["spo", "election"], name="election_spo"),
            models.UniqueConstraint(
                fields=["spo", "number"], name="number_spo")
        ]


class CountingCentre(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(unique=True)
    cco = models.ManyToManyField(
        STAFF_MODEL, related_name="counting_centres_cco")
    aro = models.ManyToManyField(
        STAFF_MODEL, related_name="counting_centres_aro")
    election = models.ManyToManyField(
        "election.Election", related_name="counting_centres")
    polling_division = models.ForeignKey(
        'PollingDivision', on_delete=models.CASCADE, related_name="counting_centres")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election", "number"], name="cc_election_number"),
            models.UniqueConstraint(
                fields=["election", "polling_division"], name="election_Polling_division"),
            models.UniqueConstraint(
                fields=["cco", "election"], name="cco_election"),
            models.UniqueConstraint(
                fields=["aro", "election"], name="aro_election")
        ]
