from django.db import models


class BusCompany(models.Model):
    name = models.CharField(max_length=50)
    head_office = models.TextField()
    staff_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

