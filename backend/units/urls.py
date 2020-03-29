from units.views import ElectoralDistrictViewSet, AdministrativeDistrictViewSet, PollingDivisionViewSet, PollingDistrictViewSet, PollingStationViewSet, CountingCentreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("electoral_district", ElectoralDistrictViewSet)
router.register("administrative_district", AdministrativeDistrictViewSet)
router.register("polling_division", PollingDivisionViewSet)
router.register("polling_district", PollingDistrictViewSet)
router.register(r'election/(?P<election>.+)/polling_station', PollingStationViewSet)
router.register(r'election/(?P<election>.+)/counting_centre', CountingCentreViewSet)

urlpatterns = router.urls
