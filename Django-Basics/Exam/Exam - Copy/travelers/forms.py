from django import forms

from travelers.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Traveler
        abstract = True
        fields = '__all__'


class TravelerCreateForm(TravelerBaseForm):
    class Meta(TravelerBaseForm.Meta):
        exclude = ['about_me']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Enter a unique nickname...'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter a valid email address...'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter a country code like <BGR>...'
            }),
        }


class TravelerEditForm(TravelerBaseForm):
    class Meta(TravelerBaseForm.Meta):
        about_label = 'About me:'
