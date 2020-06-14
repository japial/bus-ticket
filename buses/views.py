from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from buses.models import BusCompany


class CompanyList(ListView):
    model = BusCompany
    template_name = 'buses/index.html'
    context_object_name = 'buses'


class CompanyCreate(CreateView):
    model = BusCompany
    template_name = 'buses/create.html'
    fields = ('name', 'head_office', 'staff_count')
    success_url = '/buses'


class CompanyUpdate(UpdateView):
    model = BusCompany
    template_name = 'buses/update.html'
    fields = ('name', 'head_office', 'staff_count')
    success_url = '/buses'
    context_object_name = 'bus'


class CompanyDelete(DeleteView):
    model = BusCompany
    template_name = 'buses/delete.html'
    success_url = '/buses'
    context_object_name = 'bus'



