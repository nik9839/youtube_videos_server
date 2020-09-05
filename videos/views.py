from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from videos.models import Videos , YoutubeKeys
from videos.serializers import VideoListSerializer, AddKeySerializer
from videos.filters import SearchBackend

class VideosViewSet(viewsets.ReadOnlyModelViewSet):

    model = Videos
    serializer_class = VideoListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchBackend,)

    def get_queryset(self):
        """
            RETURN Videos queryset
        """

        queryset = self.model.objects.order_by("published_at") 
        
        return queryset

@api_view(["POST"])
def add_api_key(request):

    serializer = AddKeySerializer(
        data = request.data
    )
    if serializer.is_valid():
        apikey = request.data["apikey"]

        youtube_key = YoutubeKeys.objects.create(key=apikey)

        return Response({"details": "API key added"}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


