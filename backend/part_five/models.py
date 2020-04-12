from django.db import models
from staffs.models import IRARO, PDStorageInCharge
from units.models import CountingCentre
from election.models import Election
from units.models import PollingDistrict
# Create your models here.


class IssuedToAROCC(models.Model):
    issued_time = models.DateTimeField()
    i_r_aro = models.OneToOneField(
        IRARO, on_delete=models.SET_NULL, null=True, related_name="issued_to_aro_cc")
    aro_cc = models.ForeignKey(
        CountingCentre, on_delete=models.SET_NULL, null=True, related_name="issued_to_aro_cc")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="issued_to_aro_cc")
    entered_time = models.DateTimeField()
    e1 = models.IntegerField()
    zp = models.IntegerField()
    za = models.IntegerField()
    zlob = models.IntegerField()
    a = models.IntegerField()
    t2 = models.IntegerField()
    t1 = models.IntegerField()
    b = models.IntegerField()
    n = models.IntegerField()
    w = models.IntegerField()
    c = models.IntegerField()
    f = models.IntegerField()
    d = models.IntegerField()
    k = models.IntegerField()
    m = models.IntegerField()

    class Meta:
        constraints=[models.UniqueConstraint(fields=["election","entered_time","aro_cc","i_r_aro"],name="p5_arocc")]


class Cover5(models.Model):
    issued_to_aro_cc = models.OneToOneField(
        IssuedToAROCC, on_delete=models.CASCADE,related_name="cover5")
    polling_district = models.ForeignKey(
        PollingDistrict, on_delete=models.SET_NULL, null=True, related_name="cover5")

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["issued_to_aro_cc", "polling_district"], name="p5_cover5")]


class Cover6(models.Model):
    issued_to_aro_cc = models.OneToOneField(
        IssuedToAROCC, on_delete=models.CASCADE, related_name="cover6")
    polling_district = models.ForeignKey(
        PollingDistrict, on_delete=models.SET_NULL, null=True, related_name="cover6")

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["issued_to_aro_cc", "polling_district"], name="p5_cover6")]


class IssuedToPD(models.Model):
    issued_time = models.DateTimeField()
    i_r_aro = models.ForeignKey("staffs.IRARO",
                                on_delete=models.SET_NULL, null=True, related_name="issued_to_pd")
    in_charge = models.ForeignKey(
        PDStorageInCharge, on_delete=models.SET_NULL, null=True, related_name="issued_to_pd")
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True, related_name="issued_to_pd")
    entered_time = models.DateTimeField()
    st = models.IntegerField()
    tic = models.IntegerField()
    gn = models.IntegerField()
    b1 = models.IntegerField()
    pc = models.IntegerField()
    q = models.IntegerField()
    zspo = models.IntegerField()
    u1 = models.IntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["entered_time", "election", "in_charge", "i_r_aro"], name="p5_pd")]
