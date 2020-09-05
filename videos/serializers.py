import pytz
from datetime import datetime

from rest_framework import serializers
from videos.models import Videos



def _convert_datetime_to_local_timezone(request, datetime_obj):
    """

    :param datetime_obj: Datetime obj
    :param timezone: Timezone
    :return: tuple of date, time
    """
    timezone = request.query_params.get('user_timezone', 'Asia/Kolkata')

    utc_zone = pytz.timezone('UTC')
    local_timezone = pytz.timezone(timezone)

    utc = datetime_obj.replace(tzinfo=utc_zone)
    local = utc.astimezone(local_timezone)
    local_date = datetime.strftime(local, "%b %d, %Y")
    local_time = datetime.strftime(local, "%I:%M %p")

    return [local_date, local_time]

class VideoListSerializer(serializers.ModelSerializer):

    title = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    published_at = serializers.SerializerMethodField()
    thumnails = serializers.ReadOnlyField()


    class Meta:
        model = Videos
        fields = (
            'pk', 'title', 'description', 'published_at')


    def get_published_at(self, obj):
        
        if obj.published_at:
            request = self.context.get('request')
            return _convert_datetime_to_local_timezone(request, obj.published_at)
        return None



class AddKeySerializer(serializers.Serializer):

    apikey = serializers.CharField(required=True)