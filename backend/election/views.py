from rest_framework import viewsets
from election.serializers import ElectionSerializer
from election.models import Election
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class ElectionView(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

    @action(detail=False, methods=['get'])
    def get_active_elections(self, request):
        elections = Election.objects.all()
        serializer = self.get_serializer(elections, many=True)
        return Response(serializer.data)

