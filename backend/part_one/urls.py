from rest_framework import routers
from part_one.views import ReportedToWorkElectionDayViewSet, ReportedToWorkBeforeElectionViewSet

router = routers.DefaultRouter()
router.register(r'on-election-day',
                ReportedToWorkElectionDayViewSet)
router.register(r'before-election',
                ReportedToWorkBeforeElectionViewSet)

urlpatterns=router.urls
