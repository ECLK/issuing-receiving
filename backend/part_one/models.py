from django.db import models

# Create your models here.


class ReportedToWork(models.Model):
    reported_time_before_election_day = models.TimeField()
    reported_time_on_election_day = models.TimeField()
    election = models.ForeignKey(
        "election.Election", on_delete=models.SET_NULL)
