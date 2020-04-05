from django.db import models
from election.models import Election
from staffs.models import Staffs, IRARO
# Create your models here.


class ReportedToWorkElectionDay(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        Election, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.CASCADE, related_name="reported_to_work_aro_election")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["election", "staff"],name="p1_election_election_staff")
        ]


class ReportedToWorkBeforeElection(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    i_r_aro = models.ForeignKey(
        IRARO, on_delete=models.CASCADE, related_name="reported_to_work_aro_before")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election", "staff"], name="p1_before_election_staff")
        ]
