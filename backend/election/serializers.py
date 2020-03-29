from rest_framework import serializers
from election.models import Election

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields=["name","date","active","id"]