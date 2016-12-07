## Django Development With Docker Compose and Machine

Featuring:

- Docker v1.12.x
- Docker Compose v1.9.0
- Docker Machine - (Run in Ubuntu)
- Python 3.5 (With an virtul environment)

Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate todo`
1. Grab IP - `docker-machine ip dev` - and view in your browser

### Ubuntu Instructions

1. Start an virtul environment, install docker-compose
1. build images - `docker-compose build`
1. Start services -`docker-compose up -d`
1. Create Database in postgres -`psql -h 192.168.x.x -p 5432 -U postgres`
1. Create migrations -`docker-compose run web python manage.py migrate`

### Note
requirements.txt is update.
docker-compose.yml is update.
production.yml is not update.
docker-compose.yml 中的volume的路徑要用絕對路徑。
postgresql 要另建my_db
