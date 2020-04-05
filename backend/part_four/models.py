from django.db import models
from units.models import CountingCentre
from staffs.models import IRARO
from election.models import Election

# Create your models here.


class IssuedToCCO(models.Model):
    issued_time = models.DateTimeField()
    cco = models.ForeignKey(CountingCentre,
                            on_delete=models.SET_NULL, null=True, related_name="issued_to_cco")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="issued_to_cco")
    v = models.IntegerField()
    l = models.IntegerField()
    g = models.IntegerField()
    g1 = models.IntegerField()
    z = models.IntegerField()
    election = models.ForeignKey(
        Election, on_delete=models.CASCADE, related_name="issued_to_cco")
    entered_time = models.DateTimeField()

    class Meta:
        constraints=[models.UniqueConstraint(fields=["entered_time","election","i_r_aro","cco"],name="p4_cco")]


class BallotBoxesIssuedToCCO(models.Model):
    issued_cco = models.ForeignKey(IssuedToCCO, on_delete=models.CASCADE,related_name="ballot_box_issued_to_cco")
    serial_number = models.CharField(max_length=255)
