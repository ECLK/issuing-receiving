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

# Create your views here.

class IsOwner(BasePermission):
    message = "You don't have permission to access this"

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            aro = user.aro
            id = view.kwargs.get("pk")
            if id is None:
                return True
            return ReportedToWorkElectionDay.objects.get(pk=id).i_r_aro == aro
        return False

class ReportedToWorkElectionDayViewSet(viewsets.ModelViewSet):
    queryset = ReportedToWorkElectionDay.objects.all()
    serializer_class = ReportedToWorkElectionDayWriteSerializer
    serializer_action_classes = {
        'list': ReportedToWorkElectionDayReadSerializer,
        'retrieve': ReportedToWorkElectionDayReadSerializer
    }
    permission_classes=[IsOwner]

    def get_queryset(self):
        user = self.request.user
        aro = user.aro
        return ReportedToWorkElectionDay.objects.filter(i_r_aro=aro)

    def create(self, request):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                election = aro.election
                data = request.data.copy()
                data["election"] = election.id
                data["i_r_aro"] = aro.id
                report_to_work_serializer = self.get_serializer_class()(data = data)
                if (report_to_work_serializer.is_valid()):
                    report_to_work_serializer.save()
                    return Response(report_to_work_serializer.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
