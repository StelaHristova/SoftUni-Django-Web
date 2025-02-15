from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from Exam.utils import get_traveler_obj
from trips.models import Trip


class IndexPageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()

        return context


class AllTripsView(ListView):
    model = Trip
    template_name = 'trips/all-trips.html'
    ordering = ['-start_date']

