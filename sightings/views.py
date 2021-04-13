# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Squirrel
from .forms import SquirrelForm
from .forms import AddForm
from django.urls import reverse


def squirrels_list(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/squirrel_list.html', context)


def delete(request, Squirrel_ID):
    del_sighting = Squirrel.objects.filter(Unique_Squirrel_ID=Squirrel_ID)
    del_sighting.delete()
    return redirect(reverse('sightings:squirrels_list'))


def update(request, Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm(instance=squirrel)
    context = {'form': form}
    return render(request, 'sightings/update.html', context)


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = AddForm()
    context = {'form': form}
    return render(request, 'sightings/add.html', context)


def stats(request):
    gray_squirrels = Squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    adult = Squirrel.objects.filter(Age='Adult').count()
    juvenile = Squirrel.objects.filter(Age='Juvenile').count()
    am_shift = Squirrel.objects.filter(Shift='AM').count()
    above_ground = Squirrel.objects.filter(Location='Above Ground').count()
    context = {
            'gray_squirrels': gray_squirrels,
            'adult': adult,
            'juvenile': juvenile,
            'above_ground': above_ground,
            'am_shift': am_shift,
            }
    return render(request, 'sightings/stats.html', context)
