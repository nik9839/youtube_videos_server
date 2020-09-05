from celery import task 
from videos.youtube import get_youtube_data

@task(name='get_youtube_data') 
def start_youtube_background_job(args):
    get_youtube_data(args)

    