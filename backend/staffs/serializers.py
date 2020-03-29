from rest_framework import serializers
from staffs.models import Staffs, IRAROPollingDistricts, PDStorageInCharge

class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ["nic", "address", "name", "id"]
        
class IRAROSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRAROPollingDistricts
        fields = ["aro", "polling_district"]

class PDStorageInChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDStorageInCharge
        fields=["in_charge","polling_division"]
