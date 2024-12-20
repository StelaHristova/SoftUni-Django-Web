from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from profiles.forms import ProfileCreateForm
from profiles.models import Profile


class ProfileGetMixin():

    def get_object(self):
        return Profile.get_last_profile()


class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('car catalogue')
    # fields = ['username', 'email', 'age', 'password']


class ProfileDetails(ProfileGetMixin,DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = (self.object.first_name, self.object.last_name,)
        return context


class ProfileEdit(ProfileGetMixin,UpdateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('profile details')
    template_name = 'profiles/profile-edit.html'


class ProfileDelete(ProfileGetMixin,DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home page')