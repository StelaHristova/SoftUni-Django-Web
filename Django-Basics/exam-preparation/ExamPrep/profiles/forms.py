from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        model = Profile
        fields = ("username", "email", "age")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email"
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Age"
                }
            )
        }


