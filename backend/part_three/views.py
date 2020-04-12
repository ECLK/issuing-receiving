from rest_framework import viewsets
from part_three.models import ReceivedFromSPO
from part_three.serializers import ReceivedFromSPOThreeSerializer
from utils.permissions import IsOwnerVerify
from utils.mixins import AddElectionAROMixin
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(ReceivedFromSPO)
        return is_owner.verify(request, view)

# Create your views here.


class ReceivedFromSPOViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = ReceivedFromSPO.objects.all()
    serializer_class = ReceivedFromSPOThreeSerializer
    permission_classes = [IsOwner]
