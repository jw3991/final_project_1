from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView, DeleteView
#from django.db.models import Avg, Max, Min, Count

from .models import Squirrel
#from .forms import SquirrelForm


# Create your views here.

def squirrels_list(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/squirrel_list.html', context)
