from rest_framework import serializers
from part_two.models import (
    IssuedToSPO,
    BallotBoxesIssuedToSPO,
    ReceivedFromSPO,
    BallotBoxesReceived
)

class IssuedToSPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedToSPO
        fields = ["issued_time", "no_of_stamps",
                  "no_of_pens", "spo", "i_r_aro", "election", "entered_time"]

class ReceivedFromSPOSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceivedFromSPO
        fields = ["received_time", "no_of_stamps",
                  "no_of_pens", "spo", "i_r_aro", "election", "entered_time"]

class BallotBoxesIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallotBoxesIssuedToSPO
        fields = ["serial_number", "spo", "i_r_aro",
                  "election", "entered_time", "issued_time"]

class BallotBoxesReceivedSerializer(serializers.ModelSerializer):

    class Meta:
        model = BallotBoxesReceived
        fields = ["serial_number", "spo", "i_r_aro",
                  "election", "entered_time", "received_time"]
                  
