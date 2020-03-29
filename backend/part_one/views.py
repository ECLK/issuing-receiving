from rest_framework import viewsets
from part_one.models import ReportedToWorkElectionDay, ReportedToWorkBeforeElection
from part_one.serializers import (
    ReportedToWorkElectionDayWriteSerializer,
    ReportedToWorkElectionDayReadSerializer,
    ReportedToWorkBeforeReadSerializer,
    ReportedToWorkBeforeWriteSerializer
)

# Create your views here.


class ReportedToWorkElectionDayViewSet(viewsets.ModelViewSet):
    queryset = ReportedToWorkElectionDay.objects.all()
    serializer_class = ReportedToWorkElectionDayWriteSerializer
    serializer_action_classes = {
        'list': ReportedToWorkElectionDayReadSerializer,
        'retrieve': ReportedToWorkElectionDayReadSerializer
    }

    def get_queryset(self):
        election = self.kwargs['election']
        return ReportedToWorkElectionDay.objects.filter(election__id=election)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class ReportedToWorkBeforeElectionViewSet(viewsets.ModelViewSet):
    queryset = ReportedToWorkBeforeElection.objects.all()
    serializer_class = ReportedToWorkElectionDayWriteSerializer
    serializer_action_classes = {
        'list': ReportedToWorkBeforeWriteSerializer,
        'retrieve': ReportedToWorkBeforeReadSerializer
    }

    def get_queryset(self):
        election = self.kwargs['election']
        return ReportedToWorkElectionDay.objects.filter(election__id=election)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
