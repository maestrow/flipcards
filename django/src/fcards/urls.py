from django.urls import path

from . import views

urlpatterns = [
  path('sync', views.sync, name='sync'),
  path('fetch', views.fetch, name='fetch'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]
