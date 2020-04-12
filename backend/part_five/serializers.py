from rest_framework import serializers
from part_five.models import (
    IssuedToAROCC,
    Cover5,
    Cover6,
    IssuedToPD
)


class IssuedToAROCCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedToAROCC
        fields = [
            "issued_time",
            "i_r_aro",
            "aro_cc",
            "election",
            "entered_time",
            "e1",
            "zp",
            "za",
            "zlob",
            "a",
            "t2",
            "t1",
            "b",
            "n",
            "w",
            "c",
            "f",
            "d",
            "k",
            "m"
        ]

class Cover5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cover5
        fields = ["id", "issued_to_aro_cc", "polling_district"]

class Cover6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cover6
        fields = ["id", "issued_to_aro_cc", "polling_district"]

class IssuedToPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedToPD
        fields = [
            "id",
            "issued_time",
            "i_r_aro",
            "in_charge",
            "election",
            "entered_time",
            "st",
            "tic",
            "gn",
            "b1",
            "pc",
            "q",
            "zspo",
            "u1"
        ]
