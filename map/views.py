# Create your views here.
from django.shortcuts import render

from django.http import Http404

from sightings.models import Squirrel

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
        'squirrels': squirrels
    }
    return render(request, 'map/map.html', context)
