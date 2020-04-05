from django.db import models
from units.models import PollingStation
from staffs.models import IRARO
from election.models import Election
# Create your models here.


class IssuedToSPO(models.Model):
    issued_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey(
        PollingStation, on_delete=models.SET_NULL, null=True, related_name="issued_to_spo")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="issued_to_spo")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="issued_to_spo")
    entered_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["entered_time", "election", "i_r_aro", "spo"], name="p2_issued")]


class BallotBoxesIssuedToSPO(models.Model):
    serial_number = models.CharField(max_length=255)
    spo = models.ForeignKey(PollingStation,
                            on_delete=models.SET_NULL, null=True, related_name="ballot_box_issued_to_spo")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="ballot_box_issued_to_spo")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="ballot_box_issued_to_spo")
    entered_time = models.DateTimeField()
    issued_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["serial_number", "election", "entered_time"], name="p2_issued_sn_election")]


class ReceivedFromSPO(models.Model):
    received_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey(
        PollingStation, on_delete=models.SET_NULL, null=True, related_name="received_from_spo_part_two")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="received_from_spo_part_two")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="received_from_spo_part_two")
    entered_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["entered_time", "election", "i_r_aro", "spo"], name="p2_received")]


class BallotBoxesReceived(models.Model):
    serial_number = models.CharField(max_length=255)
    spo = models.ForeignKey(PollingStation,
                            on_delete=models.SET_NULL, null=True, related_name="ballot_box_received_from_spo")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="ballot_box_received_from_spo")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="ballot_box_received_from_spo")
    entered_time = models.DateTimeField()
    received_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["serial_number", "election", "entered_time"], name="p2_received_sn_election")]
