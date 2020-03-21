from django.db import models

# Create your models here.


class IssuedToSPO(models.Model):
    issued_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey(
        "units.PollingStations", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey(
        "staffs.IRAROPollingDistricts", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["entered_time", "election", "i_r_aro", "spo"], name="unique")]



class BallotBoxesIssuedToSPO(models.Model):
    serial_number = models.CharField()
    spo = models.ForeignKey("units.PollingStations", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey(
        "staffs.IRAROPollingDistrict", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    issued_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["serial_number", "election", "entered_time"],name="sn_election")]


class ReceivedFromSPO(models.Model):
    received_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey(
        "units.PollingStations", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey(
        "staffs.IRAROPollingDistricts", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["entered_time", "election", "i_r_aro", "spo"], name="unique")]


class BallotBoxesReceived(models.Model):
    serial_number = models.CharField()
    spo = models.ForeignKey("units.PollingStations", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey(
        "staffs.IRAROPollingDistrict", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    received_time = models.DateTimeField()

    class Meta:
        constraints=[models.UniqueConstraint(fields=["serial_number","election","entered_time"],name="sn_election")]
        
