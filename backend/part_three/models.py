from django.db import models
from units.models import PollingStation
from staffs.models import IRARO
from election.models import Election

# Create your models here.


class ReceivedFromSPO(models.Model):
    received_time = models.DateTimeField()
    a = models.IntegerField()
    b = models.IntegerField()
    z = models.IntegerField()
    st = models.IntegerField()
    tic = models.IntegerField()
    gn = models.IntegerField()
    b1 = models.IntegerField()
    pc = models.IntegerField()
    q = models.IntegerField()
    zspo = models.IntegerField()
    u1 = models.IntegerField()
    zlob = models.IntegerField()
    zp = models.IntegerField()
    w = models.IntegerField()
    e1 = models.IntegerField()
    l = models.IntegerField()
    t2 = models.IntegerField()
    t1 = models.IntegerField()
    g1 = models.IntegerField()
    v = models.IntegerField()
    g = models.IntegerField()
    n = models.IntegerField()
    za = models.IntegerField()
    m = models.IntegerField()
    k = models.IntegerField()
    f = models.IntegerField()
    d = models.IntegerField()
    c = models.IntegerField()
    spo = models.ForeignKey(PollingStation,
                            on_delete=models.SET_NULL, null=True, related_name="received_from_spo_part_three")
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="received_from_spo_part_three")
    election = models.ForeignKey(
        Election, on_delete=models.CASCADE, related_name="received_from_spo_part_three")
    entered_time = models.DateTimeField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["entered_time", "election", "spo", "i_r_aro"], name="p3_received")]
