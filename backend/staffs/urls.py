from rest_framework import routers
from staffs.views import StaffsViewSet, IRAROViewSet, PDStorageInChargeViewSet, IRAROPollingDistrictsViewSet

router = routers.DefaultRouter()
router.register('staffs', StaffsViewSet)
router.register('ir-aro', IRAROViewSet)
router.register('ir-aro-polling-districts', IRAROPollingDistrictsViewSet)
router.register("pd-storage-in-charge", PDStorageInChargeViewSet)

urlpatterns = router.urls
