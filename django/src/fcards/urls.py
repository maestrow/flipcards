from django.urls import path

from . import views

urlpatterns = [
  path('sync', views.sync, name='sync'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]