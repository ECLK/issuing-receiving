from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny


class ObtainTokenView(views.ObtainAuthToken):
    permission_classes = (AllowAny,)
