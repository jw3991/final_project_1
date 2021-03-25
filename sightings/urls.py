from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.squirrels_list, name='squirrels_list'),
    #path('stats', views.stats, name = 'stats'),
    #path('add/', views.add_squirrel, name = 'add'),
    #path('<str:squirrel_id>/', views.edit_squirrel, name='edit'),
]