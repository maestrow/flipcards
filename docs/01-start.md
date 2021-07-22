## Postgres

If there is no database when postgres starts in a container, then postgres will create the default database for you.
source: https://hub.docker.com/_/postgres

## Venv

```sh
python3 -m venv ./venv
source ./venv/bin/activate
```

## Install Django

```sh
python -m pip install Django
```

verify: 
```sh
python
>>> import django
>>> print(django.get_version())
3.2
```

## Creating django project

django-admin startproject flipcards
python manage.py runserver 8080
python manage.py startapp fcards