from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from buses.models import BusCompany


class CompanyList(UserPassesTestMixin, ListView):
    model = BusCompany
    template_name = 'buses/index.html'
    context_object_name = 'buses'

    def test_func(self):
        return self.request.user.has_perm('buses.view_buscompany')


class CompanyCreate(UserPassesTestMixin, CreateView):
    model = BusCompany
    template_name = 'buses/create.html'
    fields = ('name', 'head_office', 'staff_count')
    success_url = '/buses'

    def test_func(self):
        return self.request.user.has_perm('buses.add_buscompany')


class CompanyUpdate(UserPassesTestMixin, UpdateView):
    model = BusCompany
    template_name = 'buses/update.html'
    fields = ('name', 'head_office', 'staff_count')
    success_url = '/buses'
    context_object_name = 'bus'

    def test_func(self):
        return self.request.user.has_perm('buses.change_buscompany')


class CompanyDelete(UserPassesTestMixin, DeleteView):
    model = BusCompany
    template_name = 'buses/delete.html'
    success_url = '/buses'
    context_object_name = 'bus'

    def test_func(self):
        return self.request.user.has_perm('buses.delete_buscompany')




