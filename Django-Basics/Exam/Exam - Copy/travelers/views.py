from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from travelers.forms import TravelerCreateForm, TravelerEditForm
from travelers.mixins import TravelerObjectMixin
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = 'travelers/create-traveler.html'
    success_url = reverse_lazy('all-trips')


class TravelerEditView(TravelerObjectMixin, UpdateView):
    model = Traveler
    form_class = TravelerEditForm
    template_name = 'travelers/edit-traveler.html'
    success_url = reverse_lazy('traveler-details')


class TravelerDeleteView(TravelerObjectMixin, DeleteView):
    template_name = 'travelers/delete-traveler.html'
    success_url = reverse_lazy('index-page')


class TravelerDetailsView(TravelerObjectMixin, DetailView):
    model = Traveler
    template_name = 'travelers/details-traveler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        last_updated_trip_title = self.object.trips.order_by('-start_date').first()
        context['last_updated_trip_title'] = last_updated_trip_title if last_updated_trip_title else 'N/A'

        return context
