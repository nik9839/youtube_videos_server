import json
import requests
from datetime import datetime, timedelta
from django.conf import settings
from videos.models import YoutubeKeys, Videos


URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date"

def get_api_key():
    try:
        return YoutubeKeys.objects.filter(quote_reached=False).first()
    except Exception as e:
        print("No active key present. Please add key")
        return None

def set_key_expiry_status(id):
    youtube_api_key = YoutubeKeys.objects.get(id=id)
    youtube_api_key.quote_reached = True
    youtube_api_key.save()


def add_videos_in_db(videos_list):

    # Later we can use bulk create feature to add items in the table. 

    for item in videos_list:
        title =  item.get("snippet", {}).get("title", "")
        description = item.get("snippet", {}).get("description", "")
        publishedAt = item.get("snippet", {}).get("publishedAt", datetime.now())
        thumbnails = item.get("snippet", {}).get("thumbnails",{})

        video = Videos.objects.create(title=title, description=description, published_at=publishedAt,thumbnails=thumbnails)


def fetch_videos_with_api(base_url, apiKey, nextPageToken=None):
    try:
        if nextPageToken:
            base_url = base_url + "&nextPageToken=" + nextPageToken      
        # final url to use for get request
        base_url = base_url + "&key="+apiKey.key

        try:
            response = requests.request("GET", base_url) #api call
            data = json.loads(response.text)
            if data.get("error"):
                 # Currenltly for all errors api key status is changed but this can be done for only for case when quota is reached 
                
                set_key_expiry_status(apiKey.id) # Update quota flag for current apiKey 
                
                new_api_key = get_api_key()  # Get new api key and resume the operation
                if new_api_key:
                    fetch_videos_with_api(base_url, new_api_key, nextPageToken)
            else:
                # For successful response extract newPageToken and items list
                items = data.get("items", [])
                add_videos_in_db(items)  # Add videos items in DB.
                nextPageToken = data.get("nextPageToken", None)
                if nextPageToken and len(items) > 0:
                    fetch_videos_with_api(base_url, apiKey, nextPageToken)
        except Exception as e:
            print(e)
            
    except Exception as e:
        print(e)


def get_youtube_data(time_in_seconds):
    published_after = datetime.now() - timedelta(seconds=time_in_seconds)
    published_after = published_after.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get values from settings file
    videos_type = settings.YOUTUBE_API_VIDEOS_TYPE
    max_results_in_one_call = settings.YOUTUBE_API_MAX_RESULT
    
    # Create base url
    url = URL
    url = URL + "&q="+ videos_type
    url = url + "&publishedAfter=" + published_after
    url = url + "&maxResults=" + str(max_results_in_one_call)

    # Get Youtube API key 
    api_key = get_api_key()
    # IF Youtube API key then fetch data else return
    if api_key:
        fetch_videos_with_api(url, api_key, None)