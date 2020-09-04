from rest_framework.routers import SimpleRouter
from videos.views import VideosViewSet

router = SimpleRouter()

router.register(r'videos',VideosViewSet,basename='videos')

urlpatterns = router.urls