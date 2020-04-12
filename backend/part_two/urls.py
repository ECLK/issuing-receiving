from part_two.views import (
    IssuedToSpoViewSets,
    ReceivedFromSPOViewSets,
    BallotBoxesIssuedToSPOViewSets,
    BallotBoxesReceivedViewSets
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'issued-to-spo', IssuedToSpoViewSets)
router.register(r'received-from-spo', ReceivedFromSPOViewSets)
router.register(r'issued-ballot-boxes-to-spo', BallotBoxesIssuedToSPOViewSets)
router.register(r'received-ballot-boxes-from-spo', BallotBoxesReceivedViewSets)

urlpatterns=router.urls

