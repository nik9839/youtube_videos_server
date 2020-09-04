import requests
from datetime import datetime, timedelta
from celery import task 
from videos.models import YoutubeKeys, Videos
import json

def add_videos_in_db(videos_list):
    for item in videos_list:
        print(item)
        title =  item.get("snippet", {}).get("title", "")
        description = item.get("snippet", {}).get("description", "")
        publishedAt = item.get("snippet", {}).get("publishedAt", datetime.now())
        thumbnails = item.get("snippet", {}).get("thumbnails",{})

        video = Videos.objects.create(title=title, description=description, published_at=publishedAt,thumbnails=thumbnails)



@task(name='get_youtube_data') 
def get_youtube_data():
    youtube_apikey = YoutubeKeys.objects.filter(quote_reached=False).first() 
    key = youtube_apikey.key

    published_after = datetime.now() - timedelta(minutes=100)

    published_after = published_after.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(published_after)

    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=entertainment&type=video&order=date"
    url = url + "&key=" + key
    url = url + "&publishedAfter=" + published_after
    url = url + "&maxResults=" + str(50)
    print(url)

    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)

    print(json.loads(response.text))

    add_videos_in_db(json.loads(response.text)["items"])

    