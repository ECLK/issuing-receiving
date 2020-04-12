from rest_framework import viewsets
from part_five.models import (
    IssuedToAROCC,
    Cover5,
    Cover6,
    IssuedToPD
)
from part_five.serializers import (
    IssuedToAROCCSerializer,
    Cover5Serializer,
    Cover6Serializer,
    IssuedToPDSerializer
)
from utils.permissions import IsOwnerVerify, IsOwnerCoverVerify
from utils.mixins import AddElectionAROMixin, AddElectionAROCoverMixin
from rest_framework.permissions import BasePermission
# Create your views here.

message = "You don't have permission to access this"
class IsOwnerARO(BasePermission):
    message = message
    
    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(IssuedToAROCC)
        return is_owner.verify(request, view)


class IsOwnerCover5(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerCoverVerify(Cover5)
        return is_owner.verify(request, view)


class IsOwnerCover6(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerCoverVerify(Cover6)
        return is_owner.verify(request, view)


class IsOwnerPD(BasePermission):
    message = message

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(IssuedToPD)
        return is_owner.verify(request, view)

class IssuedToAROCCViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = IssuedToAROCC.objects.all()
    serializer_class = IssuedToAROCCSerializer
    permission_classes=[IsOwnerARO]


class Cover5ViewSet(AddElectionAROCoverMixin, viewsets.ModelViewSet):
    queryset = Cover5.objects.all()
    serializer_class = Cover5Serializer
    permission_classes=[IsOwnerCover5]
    

class Cover6ViewSet(AddElectionAROCoverMixin, viewsets.ModelViewSet):
    queryset = Cover6.objects.all()
    serializer_class = Cover6Serializer
    permission_classes=[IsOwnerCover6]


class IssuedToPDViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = IssuedToPD.objects.all()
    serializer_class = IssuedToPDSerializer
    permission_classes=[IsOwnerPD]

