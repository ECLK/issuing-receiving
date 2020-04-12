from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from part_one.models import ReportedToWorkElectionDay, ReportedToWorkBeforeElection
from part_one.serializers import (
    ReportedToWorkElectionDayWriteSerializer,
    ReportedToWorkElectionDayReadSerializer,
    ReportedToWorkBeforeReadSerializer,
    ReportedToWorkBeforeWriteSerializer
)
from utils.permissions import IsOwnerVerify
from utils.mixins import AddElectionAROMixin

# Create your views here.


class IsOwnerBefore(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(ReportedToWorkBeforeElection)
        return is_owner.verify(request, view)


class IsOwnerOn(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        is_owner = IsOwnerVerify(ReportedToWorkElectionDay)
        return is_owner.verify(request, view)


class ReportedToWorkElectionDayViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = ReportedToWorkElectionDay.objects.all()
    serializer_class = ReportedToWorkElectionDayWriteSerializer
    serializer_action_classes = {
        'list': ReportedToWorkElectionDayReadSerializer,
        'retrieve': ReportedToWorkElectionDayReadSerializer
    }
    permission_classes = [IsOwnerOn]

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class ReportedToWorkBeforeElectionViewSet(AddElectionAROMixin, viewsets.ModelViewSet):
    queryset = ReportedToWorkBeforeElection.objects.all()
    serializer_class = ReportedToWorkBeforeWriteSerializer
    serializer_action_classes = {
        'list': ReportedToWorkBeforeReadSerializer,
        'retrieve': ReportedToWorkBeforeReadSerializer
    }
    permission_classes = (IsOwnerBefore,)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
