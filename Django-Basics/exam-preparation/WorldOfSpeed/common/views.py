from django.shortcuts import render
from django.views.generic import TemplateView
from profiles.models import Profile


class HomePage(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['profile'] = Profile.objects.last()
        return content

