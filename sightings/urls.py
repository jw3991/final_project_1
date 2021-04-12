from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.squirrels_list, name='squirrels_list'),
    path('stats/', views.stats, name='stats'),
    path('add/', views.add, name='add'),
    path('<str:Squirrel_ID>/', views.update, name='update'),
]
