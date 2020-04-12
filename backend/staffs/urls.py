from rest_framework import routers
from staffs.views import (
    StaffsViewSet,
    IRAROViewSet,
    PDStorageInChargeViewSet,
    IRAROPollingDistrictsViewSet,
    ChangePassword,
    ChangePasswordAdmin
    )
from django.urls import path

router = routers.DefaultRouter()
router.register('staffs', StaffsViewSet)
router.register('ir-aro', IRAROViewSet)
router.register('ir-aro-polling-districts', IRAROPollingDistrictsViewSet)
router.register("pd-storage-in-charge", PDStorageInChargeViewSet)

path_one = path(r'change-password/<int:id>', ChangePasswordAdmin.as_view())
path_two = path("change-password", ChangePassword.as_view())

urlpatterns = router.urls
urlpatterns.append(path_one)
urlpatterns.append(path_two)
