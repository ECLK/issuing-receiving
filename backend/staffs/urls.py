from rest_framework import routers
from staffs.views import StaffsViewSet, IRAROViewSet, PDStorageInChargeViewSet

router = routers.DefaultRouter()
router.register('staffs', StaffsViewSet)
router.register('ir_aro', IRAROViewSet)
router.register("pd_storage_in_charge", PDStorageInChargeViewSet)

urlpatterns = router.urls
