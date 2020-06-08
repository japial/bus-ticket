from django.http import HttpRequest
from django.shortcuts import render

from buses.models import BusCompany


def bus_companies(request: HttpRequest):
    buses = BusCompany.objects.all().order_by('name')
    return render(request, 'buses/index.html', {'buses': buses})

