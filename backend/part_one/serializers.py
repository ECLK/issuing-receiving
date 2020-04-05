from rest_framework import serializers
from part_one.models import ReportedToWorkElectionDay, ReportedToWorkBeforeElection
from staffs.serializers import StaffsSerializer


class ReportedToWorkElectionDayReadSerializer(serializers.ModelSerializer):
    staff = StaffsSerializer(read_only=True)

    class Meta:
        model = ReportedToWorkElectionDay
        fields = ["id", "time", "staff","i_r_aro","election"]

class ReportedToWorkElectionDayWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedToWorkElectionDay
        fields = ["id", "time", "staff", "i_r_aro", "election"]

class ReportedToWorkBeforeReadSerializer(serializers.ModelSerializer):
    staff = StaffsSerializer(read_only=True)
    
    class Meta:
        model = ReportedToWorkBeforeElection
        fields = ["id", "time", "staff", "i_r_aro"]

class ReportedToWorkBeforeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedToWorkBeforeElection
        fields=["id","time","staff","i_r_aro"]
