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

def getEmptyResp(url):
  return {
    "url": url,
    "description": '',
    "terms": []
  }

def isCardEqual(card: models.Card, term: dict) -> bool:
  if "foreign" not in term or "meaning" not in term:
    return False
  return term["foreign"] == card.foreign and term["meaning"] == card.meaning

def getDeck(data: dict) -> models.Deck:
  url = data['url']
  metas: dict = data['metas']
  try:
    deck = models.Deck.objects.prefetch_related('cards').get(url=url)
  except models.Deck.DoesNotExist:
    deck = models.Deck(url=url)
    if 'description' in metas:
      deck.description = metas['description']
    deck.name = data['title']
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
  deck = getDeck(data)
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
    result = getEmptyResp(url)
  return result

@csrf_exempt
def sync(request: HttpRequest):
  text = request.body.decode('utf8')
  data = json.loads(text)
  if len(data['terms']) > 0:
    deck = update(data)
    result = getDeckJson(deck.url)
    return JsonResponse(result)
  else:
    # do nothing if recieved 0 items is empty
    # do not delete if deck is empty (there might be network issue on application start)
    return JsonResponse(getEmptyResp(data['url']))

@csrf_exempt
def fetch(request: HttpRequest):
  text = request.body.decode('utf8')
  data = json.loads(text)
  result = getDeckJson(data['url'])
  return JsonResponse(result)
