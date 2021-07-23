from django.core.management.base import BaseCommand
from fcards import models

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    print("Hello, world")
    card = models.Card(foreign="aaaa", meaning="bbb")
    card.save()

    first_card = models.Card.objects.all()[-1]

    print(first_card.foreign)
    print(first_card.meaning)
