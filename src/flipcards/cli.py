# https://stackoverflow.com/questions/33170016/how-to-use-django-1-8-5-orm-without-creating-a-django-project
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipcards.settings')

application = get_wsgi_application()

from fcards import models


card = models.Card(foreign="", meaning="")
card.save()

first_card = models.Card.objects.all()[0]

print(first_card.foreign)
print(first_card.meaning)
