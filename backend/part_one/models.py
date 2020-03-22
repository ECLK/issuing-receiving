from django.db import models
from election.models import Election
from staffs.models import Staffs
# Create your models here.


class ReportedToWorkElectionDay(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["election", "staff"],name="p1_election_election_staff")
        ]


class ReportedToWorkBeforeElection(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        Election, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election", "staff"], name="p1_before_election_staff")
        ]
