from part_four.models import IssuedToCCO, BallotBoxesIssuedToCCO
from part_four.serializers import IssuedToCCOSerializer, BallotBoxesIssuedToCCOSerializer
from rest_framework import viewsets
from utils.permissions import IsOwnerVerify
from utils.mixins import AddElectionAROMixin
from rest_framework.permissions import BasePermission

# Create your views here.


class IsOwner(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(IssuedToCCO)
        return is_owner.verify(request, view)


class IsOwnerBallotBoxes(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(BallotBoxesIssuedToCCO)
        return is_owner.verify(request, view)


class IssuedToCCOViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = IssuedToCCO.objects.all()
    serializer_class = IssuedToCCOSerializer
    permission_classes=[IsOwner]



class BallotBoxesIssuedToCCOViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = BallotBoxesIssuedToCCO.objects.all()
    serializer_class = BallotBoxesIssuedToCCOSerializer
    permission_classes=[IsOwnerBallotBoxes]

