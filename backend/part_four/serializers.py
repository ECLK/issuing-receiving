from rest_framework import serializers
from part_four.models import IssuedToCCO, BallotBoxesIssuedToCCO

class IssuedToCCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedToCCO
        fields = ["issued_time", "cco", "i_r_aro",
                  "v", "l", "g", "g1", "z", "election", "entered_time"]


class BallotBoxesIssuedToCCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = BallotBoxesIssuedToCCO
        fields = ["issued_cco", "serial_number"]

