from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from Exam.utils import get_traveler_obj
from trips.forms import TripCreateForm, TripDeleteForm, TripEditForm
from trips.models import Trip


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'trips/create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form):
        form.instance.traveler = get_traveler_obj()
        return super().form_valid(form)


class TripEditView(UpdateView):
    model = Trip
    form_class = TripEditForm
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/edit-trip.html'
    success_url = reverse_lazy('all-trips')


class TripDeleteView(DeleteView):
    model = Trip
    form_class = TripDeleteForm
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/delete-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class TripDetailsView(DetailView):
    model = Trip
    pk_url_kwarg = 'trip_pk'
    template_name = 'trips/details-trip.html'
