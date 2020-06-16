from django.contrib import admin

# Register your models here.
from buses.models import BusCompany, Bus


class BusInline(admin.TabularInline):
    model = Bus
    extra = 0


@admin.register(BusCompany)
class BusCompanyAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    inlines = [BusInline]


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    search_fields = ('serial_number', )
    list_display = ['serial_number', 'operator', 'seat_count']
    list_filter = ['operator']


