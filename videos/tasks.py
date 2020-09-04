from celery import task 

@task(name='get_youtube_data') 
def get_youtube_data():
    print("ok")