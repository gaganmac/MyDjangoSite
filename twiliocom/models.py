from django.core.urlresolvers import reverse_lazy
from django.db import models

# Create your models here.
from timezone_field import TimeZoneField


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='US/Pacific')

    # Additional features not visible to users
    def __str__(self):
        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse_lazy('view_appointment', args=[str(self.id)])

