from rest_framework import viewsets, status, views
from staffs.models import Staffs, IRAROPollingDistricts, IRARO, PDStorageInCharge
from staffs.serializers import (
    StaffsSerializer,
    IRAROSerializer,
    IRAROCreateSerializer,
    PDStorageInChargeSerializer,
    IRAROPollingDistrictsSerializer,
    UserSerializer
)
from units.serializers import (
    PollingDistrictSerializer,
    PollingStationSerializer,
    CountingCentreSerializer,
    PollingDivisionSerializer,
    AdministrativeDistrictSerializer,
    ElectoralDistrictSerializer
)
from election.serializers import (
    ElectionSerializer
)
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from django.contrib.auth.models import User
from utils.permissions import ReadOnly
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class StaffsViewSet(viewsets.ModelViewSet):
    queryset = Staffs.objects.all()
    serializer_class = StaffsSerializer


class IRAROViewSet(viewsets.ModelViewSet):
    queryset = IRARO.objects.all()
    serializer_class = IRAROSerializer
    permission_classes = (IsAdminUser,)
    serializer_classess={"create":IRAROCreateSerializer}

    def get_serializer_class(self):
        try:
            return self.serializer_classess[self.action]
        except (KeyError, AttributeError):
            return self.serializer_class

    def update(self, request, *args, **kwargs):
        request.data["user"]["password"] = "None"
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["GET"], permission_classes=(ReadOnly,), url_path="get-my-details")
    def get_my_details(self, request):
        """
            This allows an IR ARO to get their own details such as the electoral district
            they belong to and the polling districts under their control.
            The following information are provided:\n
                1. Electoral District
                2. Administrative District
                3. Polling Division
                4. Polling Districts
                5. Polling Stations
                6. Counting Centre
                7. Election
                8. Profile details
        """
        try:
            user = request.user
            staff = user.aro.staff
            polling_districts = []

            for pd in user.aro.polling_districts.all():
                polling_districts.append(pd.polling_district)

            polling_division = polling_districts[0].polling_division
            administrative_district = polling_division.administrative_district
            electoral_district = administrative_district.electoral_district
            election = request.user.aro.election
            polling_stations = []

            for pd in polling_districts:
                ps = pd.polling_stations.all()
                polling_stations.append(*ps.all())

            counting_centre = polling_division.counting_centres.filter(
                election=election)

            user_data = UserSerializer(user).data
            staff_data = StaffsSerializer(staff).data
            polling_districts_data = PollingDistrictSerializer(
                polling_districts, many=True).data
            polling_division_data = PollingDivisionSerializer(
                polling_division).data
            administrative_district_data = AdministrativeDistrictSerializer(
                administrative_district).data
            electoral_district_data = ElectoralDistrictSerializer(
                electoral_district).data
            election_data = ElectionSerializer(election).data
            polling_stations_data = PollingStationSerializer(
                polling_stations, many=True).data
            counting_centre_data = CountingCentreSerializer(
                counting_centre, many=True).data

            my_details = {
                "profile": dict(user_data, **staff_data),
                "polling_districts": polling_districts_data,
                "polling_division": polling_division_data,
                "administrative_district": administrative_district_data,
                "electoral_district": electoral_district_data,
                "election": election_data,
                "polling_stations": polling_stations_data,
                "counting_centre": counting_centre_data
            }

            return Response(my_details, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordAdmin(views.APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }))
    def put(self, request, id):
        """
            This allows an admin to change a user's password.
        """
        try:
            if not request.user.is_staff and not request.user.is_superuser:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            try:
                request.data["password"]
            except KeyError:
                return Response("The data format is incorrect", status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(pk=id)
            if user is None:
                return Response("A user with the provided ID is not found", status=status.HTTP_400_BAD_REQUEST)

            user.set_password(request.data["password"])
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePassword(views.APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'current_password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }))
    def put(self, request):
        """
            This allows a user to change their password.
        """
        try:
            user = request.user
            if user.check_password(request.data["current_password"]):
                user.set_password(request.data["password"])
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response("Current password is incorrect", status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response("The data format is incorrect", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class IRAROPollingDistrictsViewSet(viewsets.ModelViewSet):
    queryset = IRAROPollingDistricts.objects.all()
    serializer_class = IRAROPollingDistrictsSerializer
    permission_classes = (IsAdminUser | ReadOnly,)


class PDStorageInChargeViewSet(viewsets.ModelViewSet):
    queryset = PDStorageInCharge.objects.all()
    serializer_class = PDStorageInChargeSerializer
    permission_classes = (IsAdminUser,)

    @action(detail=False, methods=["GET"], permission_classes=(ReadOnly,),
            url_path="storage-in-charge-my-polling-division")
    def storage_in_charge_my_polling_division(self, request):
        """
            Allows an IR ARO to fetch the Polling Districts under their control.
        """
        try:
            pd = request.user.aro.polling_districts.all(
            )[0].polling_district.polling_division
            election = request.user.aro.election
            in_charge = PDStorageInCharge.objects.filter(
                polling_division=pd, election=election)
            return Response(self.get_serializer(in_charge, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
