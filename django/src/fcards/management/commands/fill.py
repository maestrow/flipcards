from django.core.management.base import BaseCommand
from fcards import models
from faker import Faker
import pprint
from django.forms.models import model_to_dict

pp = pprint.PrettyPrinter(indent=2, depth=6)

class Command(BaseCommand):

  def handle(self, *args, **kwargs):
    Faker.seed(0)
    fake = Faker()
    fakeRu = Faker(['ru-RU'])
    i = 0
    while i < 50:
      card = models.Card(
        foreign=fake.word(),
        meaning=fakeRu.word(),
        context=fake.paragraph(nb_sentences=3)
      )
      card.save()
      # pp.pprint(model_to_dict(card))
      i += 1
