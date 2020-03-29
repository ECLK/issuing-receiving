from part_four.models import IssuedToCCO, BallotBoxesIssuedToCCO
from part_four.serializers import IssuedToCCOSerializer, BallotBoxesIssuedToCCOSerializer
from rest_framework import viewsets
# Create your views here.


class IssuedToCCOViewSet(viewsets.ModelViewSet):
    queryset = IssuedToCCO.objects.all()
    serializer_class = IssuedToCCOSerializer

    def get_queryset(self):
        election = self.kwargs['election']
        return IssuedToCCO.objects.filter(election__id=election)


class BallotBoxesIssuedToCCOViewSet(viewsets.ModelViewSet):
    queryset = BallotBoxesIssuedToCCO.objects.all()
    serializer_class = BallotBoxesIssuedToCCOSerializer

    def get_queryset(self):
        election = self.kwargs["election"]
        return BallotBoxesIssuedToCCO.objects.filter(election__id=election)
