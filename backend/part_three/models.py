from django.db import models

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
    spo = models.ForeignKey("staffs.Staffs", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    id = models.AutoField()

    class Meta:
        unique_together = (("entered_time", "id"))
