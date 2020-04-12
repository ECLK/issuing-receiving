from rest_framework.response import Response
from rest_framework import status


class AddElectionAROMixin:
    def create(self, request):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                election = aro.election
                data = request.data.copy()
                data["election"] = election.id
                data["i_r_aro"] = aro.id
                serializer = self.get_serializer_class()(data=data)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                election = aro.election
                data = request.data.copy()
                data["election"] = election.id
                data["i_r_aro"] = aro.id
                serializer = self.get_serializer(
                    self.get_object(), data=data)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                election = aro.election
                data = request.data.copy()
                data["election"] = election.id
                data["i_r_aro"] = aro.id
                serializer = self.get_serializer(
                    self.get_object(), data=data, partial=True)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        aro = user.aro
        return self.queryset.filter(i_r_aro=aro)


class AddElectionAROCoverMixin:
    def create(self, request):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                issued = aro.issued_to_aro_cc
                data = request.data.copy()
                data["issued_to_aro_cc"] = issued.id
                serializer = self.get_serializer_class()(data=data)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                issued = aro.issued_to_aro_cc
                data = request.data.copy()
                data["issued_to_aro_cc"] = issued
                serializer = self.get_serializer(
                    self.get_object(), data=data)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            user = self.request.user
            if user.is_authenticated:
                aro = user.aro
                issued = aro.issued_to_aro_cc
                data = request.data.copy()
                data["issued_to_aro_cc"] = issued
                serializer = self.get_serializer(
                    self.get_object(), data=data, partial=True)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        aro = user.aro
        issued = aro.issued_to_aro_cc
        return self.queryset.filter(issued_to_aro_cc=issued)
