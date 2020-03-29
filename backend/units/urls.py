from units.views import ElectoralDistrictViewSet, AdministrativeDistrictViewSet, PollingDivisionViewSet, PollingDistrictViewSet, PollingStationViewSet, CountingCentreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("electoral-district", ElectoralDistrictViewSet)
router.register("administrative-district", AdministrativeDistrictViewSet)
router.register("polling-division", PollingDivisionViewSet)
router.register("polling-district", PollingDistrictViewSet)
router.register(r'election/(?P<election>.+)/polling-station', PollingStationViewSet)
router.register(r'election/(?P<election>.+)/counting-centre', CountingCentreViewSet)

urlpatterns = router.urls
