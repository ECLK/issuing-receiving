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
# Create your views here.

class IssuedToAROCCViewSet(viewsets.ModelViewSet):
    queryset = IssuedToAROCC.objects.all()
    serializer_class = IssuedToAROCCSerializer
    
    def get_queryset(self):
        election = self.kwargs["election"]
        return IssuedToAROCC.objects.filter(election__id=election)


class Cover5ViewSet(viewsets.ModelViewSet):
    queryset = Cover5.objects.all()
    serializer_class = Cover5Serializer
    
    def get_queryset(self):
        election = self.kwargs["election"]
        return Cover5.objects.filter(election__id=election)

class Cover6ViewSet(viewsets.ModelViewSet):
    queryset = Cover6.objects.all()
    serializer_class = Cover6Serializer
    
    def get_queryset(self):
        election = self.kwargs["election"]
        return Cover6.objects.filter(election__id=election)


class IssuedToPDViewSet(viewsets.ModelViewSet):
    queryset = IssuedToPD.objects.all()
    serializer_class = IssuedToPDSerializer
    
    def get_queryset(self):
        election = self.kwargs["election"]
        return IssuedToPD.objects.filter(election__id=election)
