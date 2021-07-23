## Postgres

If there is no database when postgres starts in a container, then postgres will create the default database for you.
source: https://hub.docker.com/_/postgres

## Venv

```sh
python3 -m venv ./venv
source ./venv/bin/activate
```

## Install Django

Follow the [tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

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

## Configure django with Postgres

### Install postgresql-client and psycopg2

source: https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django

To get Python working with Postgres, you will need to install the "psycopg2" module. However, you must first have pg_config installed on your OS.

If you can’t find `pg_config` on your OS, you will need to install a Postgres client first. 

```sh
sudo apt install postgresql-client # may be unnecessary
sudo apt install postgresql-common libpq-dev
pg_config # check
pip install psycopg2
```

### Db Settings

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flipcards',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### Run initial migration

`./manage.py migrate`

### Next: Create models

Continue tutorial: https://docs.djangoproject.com/en/3.2/intro/tutorial02/