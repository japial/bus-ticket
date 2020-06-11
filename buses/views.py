from django.http import HttpRequest
from django.shortcuts import render

from buses.models import BusCompany


def index(request: HttpRequest):
    buses = BusCompany.objects.all().order_by('name')
    return render(request, 'buses/index.html', {'buses': buses})


def update(request: HttpRequest, pk):
    bus = BusCompany.objects.get(id=pk)
    if request.method == 'POST':
        bus.name = request.POST.get('name')
        bus.head_office = request.POST.get('head_office')
        bus.staff_count = request.POST.get('staff_count')
        bus.save()

    return render(request, 'buses/update.html', {'bus': bus})