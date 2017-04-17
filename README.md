## Django Development With Docker Compose and Machine

Featuring:

- Docker v1.17.x
- Docker Compose v1.12.0
- Python 3.6 (With an virtul environment)

Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate todo`
1. Grab IP - `docker-machine ip dev` - and view in your browser

### Ubuntu Instructions

1. Start a python virtul environment, `pip install docker-compose`
1. build images - `docker-compose build`
1. Start services -`docker-compose up -d`
1. Create Database in postgres -`psql -h 192.168.x.x -p 5432 -U postgres` `create database my_db` `\l` check List of databases.
1. Create migrations -`docker-compose run web python manage.py migrate`

### Note
requirements.txt is update.
docker-compose.yml is update.
production.yml is not update.
If you have old pgdata volume, remember delete it, or your will get errors.

```
postgres_1  | FATAL:  database files are incompatible with server
postgres_1  | DETAIL:  The data directory was initialized by PostgreSQL version 9.5, which is not compatible with this version 9.6.2.
```
docker-compose.yml 中的volume的路徑要用絕對路徑。
postgresql 要另建my_db

Dockerfile of nginx changed.
Dockerfile of web update to python:3.6

update in 2017/04/16.