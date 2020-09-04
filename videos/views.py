from rest_framework import viewsets
from videos.models import Videos
from videos.serializers import VideoListSerializer


class VideosViewSet(viewsets.ReadOnlyModelViewSet):

    model = Videos
    serializer_class = VideoListSerializer

    def get_queryset(self):
        """
            RETURN Videos queryset
        """

        queryset = self.model.objects.order_by("id") 
        
        return queryset
    