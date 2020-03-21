from django.db import models

# Create your models here.


class IssuedToAROCC(models.Model):
    issued_time = models.DateTimeField()
    i_r_aro = models.ForeignKey("staffs.IRAROPollingDistricts", on_delete=models.SET_NULL)
    aro_cc = models.ForeignKey("units.CountingCentre", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
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
        constraints=[models.UniqueConstraint(fields=["election","entered_time","aro_cc","i_r_aro"])]


class Cover5(models.Model):
    issued_to_aro_cc = models.ForeignKey(
        "IssuedToAROCC", on_delete=models.CASCADE)
    polling_district = models.ForeignKey(
        "units.PollingDistricts", on_delete=models.SET_NULL)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["issued_to_aro_cc", "polling_district"])]


class Cover6(models.Model):
    issued_to_aro_cc = models.ForeignKey(
        "IssuedToAROCC", on_delete=models.CASCADE)
    polling_district = models.ForeignKey(
        "units.PollingDistricts", on_delete=models.SET_NULL)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["issued_to_aro_cc", "polling_district"])]


class IssuedToPD(models.Model):
    issued_time = models.DateTimeField()
    i_r_aro = models.ForeignKey("staffs.IRAROPollingDistricts", on_delete=models.SET_NULL)
    in_charge = models.ForeignKey("staffs.PDStorageInCharge", on_delete=models.SET_NULL)
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
    entered_time = models.DateTimeField()
    id = models.AutoField()
    st = models.IntegerField()
    tic = models.IntegerField()
    gn = models.IntegerField()
    b1 = models.IntegerField()
    pc = models.IntegerField()
    q = models.IntegerField()
    zspo = models.IntegerField()
    u1 = models.IntegerField()

    class Meta:
        constraints=[models.UniqueConstraint(fields=["entered_time","election","in_charge","i_r_aro"])]
