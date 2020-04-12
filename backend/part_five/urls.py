from rest_framework import routers
from part_five.views import (
    IssuedToAROCCViewSet,
    Cover5ViewSet,
    Cover6ViewSet,
    IssuedToPDViewSet
)

router = routers.DefaultRouter()
router.register(r'issued-to-aro-cc',
                IssuedToAROCCViewSet)
router.register(r'cover-5',
                Cover5ViewSet)
router.register(r'cover-6',
                Cover6ViewSet)
router.register(r'issued-to-pd',
                IssuedToPDViewSet)

urlpatterns = router.urls

