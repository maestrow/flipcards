from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def sync(request):
  text = request.body.decode('utf8')
  data = json.loads(text)
  return JsonResponse({'foo': data})


def vote(request, question_id):
   return HttpResponse("You're voting on question %s." % question_id)