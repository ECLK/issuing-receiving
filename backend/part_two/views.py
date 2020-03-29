from part_two.models import (
    IssuedToSPO,
    BallotBoxesIssuedToSPO,
    ReceivedFromSPO,
    BallotBoxesReceived
)
from rest_framework import viewsets
from part_two.serializers import (
    IssuedToSPOSerializer,
    ReceivedFromSPOSerializer,
    BallotBoxesIssuedSerializer,
    BallotBoxesReceivedSerializer
)

# Create your views here.

class IssuedToSpoViewSets(viewsets.ModelViewSet):
    queryset = IssuedToSPO.objects.all()
    serializer_class = IssuedToSPOSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return IssuedToSPO.objects.filter(election__id=election)

class ReceivedFromSPOViewSets(viewsets.ModelViewSet):
    queryset = ReceivedFromSPO.objects.all()
    serializer_class = ReceivedFromSPOSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return ReceivedFromSPO.objects.filter(election__id=election)


class BallotBoxesIssuedToSPOViewSets(viewsets.ModelViewSet):
    queryset = BallotBoxesIssuedToSPO.objects.all()
    serializer_class = BallotBoxesIssuedSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return BallotBoxesIssuedToSPO.objects.filter(election__id=election)

class BallotBoxesReceivedViewSets(viewsets.ModelViewSet):
    queryset = BallotBoxesReceived.objects.all()
    serializer_class = BallotBoxesReceivedSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return BallotBoxesReceived.objects.filter(election__id=election)


