from django.db import models

# Create your models here.


class ReportedToWorkElectionDay(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["election, staff"],name="p1_election_election_staff")
        ]


class ReportedToWorkBeforeElection(models.Model):
    time = models.TimeField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey("staffs.Staffs", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["election, staff"], name="p1_before_election_staff")
        ]
