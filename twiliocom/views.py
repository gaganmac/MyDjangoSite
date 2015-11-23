from django.core.urlresolvers import reverse_lazy

from .models import Appointment
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

# Create your views here.


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create new appointment"""

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully created.'


class AppointmentListView(ListView):
    """Shows users a list of appointments"""
    model = Appointment


class AppointmentDetailView(DetailView):
    """Shows users a single appointment"""
    model = Appointment


class AppointmentDeleteView(DeleteView):
    """ Prompts users to confirm deleting an appointment"""

    model = Appointment
    success_url = reverse_lazy('list_appointment')


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    """ Powers a form to edit existing appointments """

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully updated.'

