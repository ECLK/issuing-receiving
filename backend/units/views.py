from rest_framework import viewsets
from units.serializers import (
    ElectoralDistrictSerializer,
    AdministrativeDistrictSerializer,
    PollingDivisionSerializer,
    PollingDistrictSerializer,
    PollingStationSerializer,
    CountingCentreSerializer
    )
from units.models import (
    ElectoralDistrict,
    AdministrativeDistrict,
    PollingDivision,
    PollingDistrict,
    PollingStation,
    CountingCentre
)

# Create your views here.


class ElectoralDistrictViewSet(viewsets.ModelViewSet):
    queryset = ElectoralDistrict.objects.all()
    serializer_class = ElectoralDistrictSerializer


class AdministrativeDistrictViewSet(viewsets.ModelViewSet):
    queryset = AdministrativeDistrict.objects.all()
    serializer_class = AdministrativeDistrictSerializer


class PollingDivisionViewSet(viewsets.ModelViewSet):
    queryset = PollingDivision.objects.all()
    serializer_class = PollingDivisionSerializer


class PollingDistrictViewSet(viewsets.ModelViewSet):
    queryset = PollingDistrict.objects.all()
    serializer_class = PollingDistrictSerializer


class PollingStationViewSet(viewsets.ModelViewSet):
    queryset = PollingStation.objects.all()
    serializer_class = PollingStationSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return PollingStation.objects.filter(election__id=election)


class CountingCentreViewSet(viewsets.ModelViewSet):
    queryset = CountingCentre.objects.all()
    serializer_class = CountingCentreSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return PollingStation.objects.filter(election__id=election)
