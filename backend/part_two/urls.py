from part_two.views import (
    IssuedToSpoViewSets,
    ReceivedFromSPOViewSets,
    BallotBoxesIssuedToSPOViewSets,
    BallotBoxesReceivedViewSets
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'election/(?P<election>.*)/issued-to-spo/', IssuedToSpoViewSets)
router.register(r'election/(?P<election>.*)/received-from-spo', ReceivedFromSPOViewSets)
router.register(r'election/(?P<election>.*)/issued-ballot-boxes-to-spo', BallotBoxesIssuedToSPOViewSets)
router.register(r'election/(?P<election>.*)/received-ballot-boxes-from-spo', BallotBoxesReceivedViewSets)

urlpatterns=router.urls

