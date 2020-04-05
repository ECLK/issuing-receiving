from rest_framework import serializers
from staffs.models import Staffs, IRAROPollingDistricts, PDStorageInCharge, IRARO
from django.contrib.auth.models import User


class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ["nic", "address", "name", "id"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "is_superuser", "is_staff"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class IRAROSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = IRARO
        fields = ["staff", "election", "user", "id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = self.fields["user"].create(user_data)
        validated_data["user"] = user
        iraro = IRARO.objects.create(**validated_data)
        return iraro


class IRAROPollingDistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRAROPollingDistricts
        fields = "__all__"


class PDStorageInChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDStorageInCharge
        fields = ["in_charge", "polling_division","election","id"]
