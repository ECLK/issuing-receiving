from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
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
from rest_framework.permissions import IsAdminUser
from utils.permissions import ReadOnly
# Create your views here.


class ElectoralDistrictViewSet(viewsets.ModelViewSet):
    queryset = ElectoralDistrict.objects.all()
    serializer_class = ElectoralDistrictSerializer
    permission_classes = (IsAdminUser,)


class AdministrativeDistrictViewSet(viewsets.ModelViewSet):
    queryset = AdministrativeDistrict.objects.all()
    serializer_class = AdministrativeDistrictSerializer
    permission_classes = (IsAdminUser,)


class PollingDivisionViewSet(viewsets.ModelViewSet):
    queryset = PollingDivision.objects.all()
    serializer_class = PollingDivisionSerializer
    permission_classes = (IsAdminUser,)


class PollingDistrictViewSet(viewsets.ModelViewSet):
    queryset = PollingDistrict.objects.all()
    serializer_class = PollingDistrictSerializer
    permission_classes = (IsAdminUser,)


class PollingStationViewSet(viewsets.ModelViewSet):
    queryset = PollingStation.objects.all()
    serializer_class = PollingStationSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        election = self.kwargs['election']
        return PollingStation.objects.filter(election__id=election)
    

    @action(detail=False, methods=["GET"], permission_classes=(ReadOnly,), url_path="polling-stations-under-control")
    def polling_stations_under_control(self, request, election):
        try:
            polling_districts = request.user.aro.polling_districts.all()
            aro_polling_stations = []
            for pd in polling_districts:
                polling_stations=pd.polling_district.polling_stations.all()
                aro_polling_stations.append(*polling_stations.all())
            serializer = self.get_serializer(aro_polling_stations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response (status.HTTP_500_INTERNAL_SERVER_ERROR)



class CountingCentreViewSet(viewsets.ModelViewSet):
    queryset = CountingCentre.objects.all()
    serializer_class = CountingCentreSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        election = self.kwargs['election']
        return CountingCentre.objects.filter(election__id=election)

    @action(detail=False, methods=["GET"], permission_classes=(ReadOnly,), url_path="counting-centre-of-my-pd")
    def counting_centre_of_my_pd(self, request, election):
        try:
            polling_districts = request.user.aro.polling_districts.all()
            polling_division = polling_districts[0].polling_district.polling_division
            election=request.user.aro.election
            counting_centres = CountingCentre.objects.filter(polling_division = polling_division, election = election)
            return Response(self.get_serializer(counting_centres, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
