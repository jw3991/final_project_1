# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404 ,redirect
from .models import Squirrel
from .forms import SquirrelForm
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView
# from django.db.models import Avg, Max, Min, Count


def squirrels_list(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/squirrel_list.html', context)


def update(request, Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm(instance=squirrel)
    context = {'form': form}
    return render(request, 'sightings/update.html', context)
