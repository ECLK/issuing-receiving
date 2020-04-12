from part_two.models import (
    IssuedToSPO,
    BallotBoxesIssuedToSPO,
    ReceivedFromSPO,
    BallotBoxesReceived
)
from rest_framework import viewsets
from part_two.serializers import (
    IssuedToSPOSerializer,
    ReceivedFromSPOSerializer,
    BallotBoxesIssuedSerializer,
    BallotBoxesReceivedSerializer
)
from utils.permissions import IsOwnerVerify
from rest_framework.permissions import BasePermission
from utils.mixins import AddElectionAROMixin


message = "You don't have permission to access this"


class IsOwnerIssuedToSPO(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(IssuedToSPO)
        return is_owner.verify(request, view)

class IsOwnerReceivedFromSPO(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(ReceivedFromSPO)
        return is_owner.verify(request, view)

class IsOwnerBallotBoxesIssued(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(BallotBoxesIssuedToSPO)
        return is_owner.verify(request, view)


class IsOwnerBallotBoxesReceived(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(BallotBoxesReceived)
        return is_owner.verify(request, view)
        

# Create your views here.

class IssuedToSpoViewSets(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = IssuedToSPO.objects.all()
    serializer_class = IssuedToSPOSerializer
    permission_classes=[IsOwnerIssuedToSPO]



class ReceivedFromSPOViewSets(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = ReceivedFromSPO.objects.all()
    serializer_class = ReceivedFromSPOSerializer
    permission_classes=[IsOwnerReceivedFromSPO]



class BallotBoxesIssuedToSPOViewSets(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = BallotBoxesIssuedToSPO.objects.all()
    serializer_class = BallotBoxesIssuedSerializer
    permission_classes=[IsOwnerBallotBoxesIssued]



class BallotBoxesReceivedViewSets(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = BallotBoxesReceived.objects.all()
    serializer_class = BallotBoxesReceivedSerializer
    permission_classes=[IsOwnerReceivedFromSPO]



