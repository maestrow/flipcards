from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from fcards import models
import typing

# Create your views here.

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

# sync

def isCardEqual(card: models.Card, term: dict) -> bool:
  if "foreign" not in term or "meaning" not in term:
    return False
  return term["foreign"] == card.foreign and term["meaning"] == card.meaning

def getDeck(url, metas: dict) -> models.Deck:
  try:
    deck = models.Deck.objects.prefetch_related('cards').get(url=url)
  except models.Deck.DoesNotExist:
    deck = models.Deck(url=url)
    if 'description' in metas:
      deck.description = metas['description']
    deck.save()
  return deck

def updateCard(deck: models.Deck, foreign, meaning, context) -> models.Card:
  try:
    card: models.Card = models.Card.objects.get(foreign=foreign, meaning=meaning)
  except models.Card.DoesNotExist:
    card: models.Card = models.Card(foreign=foreign, meaning=meaning, context=context)
    card.save()
  try:
    deck.cards.get(pk=card.pk)
  except models.Card.DoesNotExist:
    deck.cards.add(card)

def update(data: dict) -> models.Deck:
  deck = getDeck(data['url'], data['metas'])
  terms: list[dict] = data['terms']

  # delete
  for card in deck.cards.all():
    f = list(filter(lambda t: isCardEqual(card, t), terms))
    if not f:
      print("removing: {} - {}".format(card.foreign, card.meaning))
      deck.cards.remove(card)

  # create / update
  for term in data['terms']:
    updateCard(
      deck,
      term['foreign'],
      term['meaning'],
      term['context']
    )
  return deck

def toJson(deck: models.Deck) -> dict:
  terms = []
  for card in deck.cards.all():
    terms.append({
      "foreign": card.foreign,
      "meaning": card.meaning,
      "context": card.context
    })
  return {
    "url": deck.url,
    "description": deck.description,
    "terms": terms
  }

def getDeckJson(url: str) -> dict:
  result: dict
  try:
    deck = models.Deck.objects.prefetch_related('cards').get(url=url)
    result = toJson(deck)
  except models.Deck.DoesNotExist:
    resutl = {
      "url": url,
      "description": '',
      "terms": []
    }
  return result

@csrf_exempt
def sync(request: HttpRequest):
  text = request.body.decode('utf8')
  data = json.loads(text)
  deck = update(data)
  result = getDeckJson(deck.url)
  return JsonResponse(result)


@csrf_exempt
def fetch(request: HttpRequest):
  text = request.body.decode('utf8')
  data = json.loads(text)
  result = getDeckJson(data['url'])
  return JsonResponse(result)
