from django.db import models

# Create your models here.


class IssuedToSPO(models.Model):
    issued_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    id = models.AutoField()

    class Meta:
        unique_together = (("entered_time", "id"))


class BallotBoxesIssued(models.Model):
    serial_number = models.CharField()
    issued_to_spo = models.ForeignKey("IssuedToSPO", on_delete=models.CASCADE)


class ReceivedFromSPO(models.Model):
    received_time = models.DateTimeField()
    no_of_stamps = models.IntegerField()
    no_of_pens = models.IntegerField()
    spo = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    i_r_aro = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    id = models.AutoField()

    class Meta:
        unique_together = (("entered_time", "id"))


class BallotBoxesReceived(models.Model):
    serial_number = models.CharField()
    received_from_spo = models.ForeignKey(
        "ReceivedFromSPO", on_delete=models.CASCADE)
