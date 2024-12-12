from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    # class Meta:
    #     model = Profile
    #     fields = "__all__"
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm):
        model = Profile
        fields = ("username", "email", "age", "password")