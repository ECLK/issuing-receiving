from rest_framework import routers
from election.views import ElectionView

router = routers.DefaultRouter()
router.register(r'', ElectionView)

urlpatterns = router.urls
