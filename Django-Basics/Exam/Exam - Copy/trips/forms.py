from django import forms

from Exam.mixins import LabelAddMixin, ReadOnlyMixin
from trips.models import Trip


class TripBaseForm(LabelAddMixin, forms.ModelForm):
    destination_label = 'Destination:'
    summary_label = 'Summary:'
    start_label = 'Started on:'
    duration_label = 'Duration:'
    image_label = 'Image URL:'

    class Meta:
        model = Trip
        exclude = ['traveler']


class TripCreateForm(TripBaseForm):
    class Meta(TripBaseForm.Meta):
        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': 'Enter a short destination note...'
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Share your exciting moments...'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'image_url': forms.TextInput(attrs={
                'placeholder': 'An optional image URL...'
            }),
        }
        help_texts = {
            'duration': '*Duration in days is expected.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration'].initial = 1

        
class TripEditForm(TripBaseForm):
    pass


class TripDeleteForm(ReadOnlyMixin, TripBaseForm):
    pass
    