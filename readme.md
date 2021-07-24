source ./venv/bin/activate

pip freeze > requirements.txt
pip install -r requirements.txt

./manage.py makemigrations fcards
./manage.py migrate
./manage.py runserver

# ToDo

- избавиться от pycache