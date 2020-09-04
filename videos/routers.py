from django.urls import re_path, include

from rest_framework.routers import SimpleRouter
from videos.views import VideosViewSet, add_api_key

router = SimpleRouter()

router.register(r'videos',VideosViewSet,basename='videos')

urlpatterns = [
    re_path(r'^add-api-key/$', add_api_key, name='add-api-key'),
]
urlpatterns = urlpatterns + router.urls

