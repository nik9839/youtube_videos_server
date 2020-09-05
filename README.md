# Youtube Videos

Django server for vidoes platform. The database used is PostgreSQL.
REDIS & celery is used for handling asynchronus task.

## Run using Docker

 - Install docker & docker compose
 - Update the environment variables as needed.
 - Variables - `GET_DATA_AFTER_EVERY_X_SECONDS` ,  `YOUTUBE_API_VIDEOS_TYPE` , `YOUTUBE_API_MAX_RESULT`
 - RUN command `docker-compose build` to build images.
 - RUN command `docker-compose up` to start the docker container.
 - RUN command `docker ps` to get the web container name.
 - RUN command `docker exce -it {container_name} bash` to get inside container.
 - Inside the container run command `./manage.py migrate` to run migrations on db.
 - Use api 'http://localhost:8000/add-api-key/` to add apikey to db. 

## Run locally 

 - Create POSTGRES DATABASE if not present
 - Create Redis server if not present
 - Create virtual environment `python3.6 -m venev youtube_videos`
 - Activate the environment `source youtube_videos/bin/activate`
 - RUN command `pip install -r requirement.txt` to install packages.
 - UPDATE DATABSE config in the settings file `youtube_videos/settings.py`
 - UPDATE `GET_DATA_AFTER_EVERY_X_SECONDS` ,  `YOUTUBE_API_VIDEOS_TYPE` , `YOUTUBE_API_MAX_RESULT`, `REDIS_HOST` if needed.
 - RUN command `./manage.py runserver` to start the api server.
 - RUN command `celery -A youtube_videos worker -B -l INFO` for run celery for async task. 


## Postman API Collection

https://www.getpostman.com/collections/f24cf279e5a9b88b41e1


