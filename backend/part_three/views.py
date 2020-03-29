from rest_framework import viewsets
from part_three.models import ReceivedFromSPO
from part_three.serializers import ReceivedFromSPOSerializer

# Create your views here.

class ReceivedFromSPOViewSet(viewsets.ModelViewSet):
    queryset = ReceivedFromSPO.objects.all()
    serializer_class = ReceivedFromSPOSerializer

    def get_serializer_class(self):
        election = self.kwargs['election']
        return ReceivedFromSPO.objects.filter(election__id=election)
