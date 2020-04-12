from rest_framework import serializers
from staffs.models import Staffs, IRAROPollingDistricts, PDStorageInCharge, IRARO
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = ["nic", "address", "name", "id"]


class UserNoPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

    def validate_username(self, value):
        if User.objects.get(username=value) is None:
            return value
        else:
            if User.objects.get(username=value).id == self.parent.instance.user.id:
                return value
            else:
                raise serializers.ValidationError(
                    "The username already exists.")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            "username": {
                "validators": [UnicodeUsernameValidator]
            }
        }

    def create(self, validated_data):
        validated_data["is_superuser"] = False
        validated_data["is_staff"] = False
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance


class IRAROCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = IRARO
        fields = ["staff", "election", "user", "id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = self.fields["user"].create(user_data)
        validated_data["user"] = user
        try:
            iraro = IRARO.objects.create(**validated_data)
            return iraro
        except:
            User.objects.get(User).delete()

class IRAROSerializer(serializers.ModelSerializer):
    user = UserNoPasswordSerializer()
    
    class Meta:
        model = IRARO
        fields=["staff", "election", "user", "id"]
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = self.fields["user"].update(instance.user, user_data)
        user_copy = instance.user
        instance.user = user
        try:
            instance.staff = validated_data.get("staff", instance.staff)
            instance.election = validated_data.get(
                "election", instance.election)
            instance.save()
            return instance
        except:
            user_copy.save()


class IRAROPollingDistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRAROPollingDistricts
        fields = "__all__"


class PDStorageInChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDStorageInCharge
        fields = ["in_charge", "polling_division", "election", "id"]
