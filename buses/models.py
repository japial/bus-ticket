from django.db import models


class BusCompany(models.Model):
    name = models.CharField(max_length=50)
    head_office = models.TextField()
    staff_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bus Companies'


class Bus(models.Model):
    serial_number = models.CharField(max_length=15, db_index=True)
    operator = models.ForeignKey('BusCompany', on_delete=models.CASCADE)
    seat_count = models.IntegerField(default=0)

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name_plural = 'Buses'

