from rest_framework import serializers
from part_three.models import ReceivedFromSPO

class ReceivedFromSPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedFromSPO
        fields = [
            "received_time",
            "a",
            "b",
            "z",
            "st",
            "tic",
            "gn",
            "b1",
            "pc",
            "q",
            "zspo",
            "u1",
            "zlob",
            "zp",
            "w",
            "e1",
            "l",
            "t2",
            "t1",
            "g1",
            "v",
            "g",
            "n",
            "za",
            "m",
            "k",
            "f",
            "d",
            "c",
            "spo",
            "i_r_aro",
            "election",
            "entered_time"
        ]
