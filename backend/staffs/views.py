from rest_framework import viewsets
from staffs.models import Staffs, IRAROPollingDistricts, PDStorageInCharge
from staffs.serializers import StaffsSerializer, IRAROSerializer, PDStorageInChargeSerializer

# Create your views here.

class StaffsViewSet(viewsets.ModelViewSet):
    queryset = Staffs.objects.all()
    serializer_class = StaffsSerializer
    
class IRAROViewSet(viewsets.ModelViewSet):
    queryset = IRAROPollingDistricts.objects.all()
    serializer_class = IRAROSerializer

class PDStorageInChargeViewSet(viewsets.ModelViewSet):
    queryset = PDStorageInCharge.objects.all()
    serializer_class = PDStorageInChargeSerializer
