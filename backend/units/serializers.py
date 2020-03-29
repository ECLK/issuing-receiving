from rest_framework import serializers
from units.models import ElectoralDistrict, AdministrativeDistrict, PollingDivision, PollingDistrict, PollingStation, CountingCentre

class ElectoralDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectoralDistrict
        fields = ["name", "id"]
    
class AdministrativeDistrictSerializer(serializers.ModelSerializer):
    class Meta:    
        model = AdministrativeDistrict
        fields = ["name", "electoral_district"]
    
class PollingDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingDivision
        fields = ["name", "administrative_district"]

class PollingDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingDistrict
        fields = ["name", "polling_division"]
    
class PollingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingStation
        fields=["election","number","spo","election","polling_district"]

class CountingCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountingCentre
        fields = ["name", "number", "cco", "aro", "election", "polling_division"]
        