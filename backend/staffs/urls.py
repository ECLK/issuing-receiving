from rest_framework import routers
from staffs.views import StaffsViewSet, IRAROViewSet, PDStorageInChargeViewSet

router = routers.DefaultRouter()
router.register('staffs', StaffsViewSet)
router.register('ir-aro', IRAROViewSet)
router.register("pd-storage-in-charge", PDStorageInChargeViewSet)

urlpatterns = router.urls
