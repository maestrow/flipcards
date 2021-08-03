from django.db import models


class Card(models.Model):
  foreign = models.CharField(max_length=200)
  meaning = models.CharField(max_length=200)
  pronunciation = models.CharField(max_length=200, null=True)
  context = models.CharField(max_length=2000, null=True)
  notes = models.TextField(null=True)
  last_review = models.DateTimeField(null=True)
  n = models.IntegerField(
    default=0,
    verbose_name="Repetition number",
    help_text="""The repetition number n, which is the number of times the card has been
    successfully recalled in a row since the last time it was not.""")
  i = models.IntegerField(
    default=0,
    verbose_name="Interval",
    help_text="""The inter-repetition interval I, which is the length of time (in days)
    SuperMemo will wait after the previous review before asking the user to review the card again.""")
  ef = models.FloatField(
    default=2.5,
    verbose_name="Easiness Factor",
    help_text="""The easiness factor EF, which loosely indicates how easy the card is
    (more precisely, it determines how quickly the inter-repetition interval grows).
    The initial value of EF is 2.5.""")

  class Meta:
    db_table = "card"
    constraints = [
      models.UniqueConstraint(fields=['foreign', 'meaning'], name='unique_foreign_meaning')
    ]


class Deck(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  url = models.CharField(max_length=2000, unique=True)
  cards = models.ManyToManyField(Card)

  class Meta:
    db_table = "deck"

class Tag(models.Model):
  name = models.CharField(max_length=200, unique=True)
  description = models.TextField()
  decks = models.ManyToManyField(Deck)

  class Meta:
    db_table = "tag"
