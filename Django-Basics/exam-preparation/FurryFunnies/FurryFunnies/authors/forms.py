from django import forms

from FurryFunnies.mixins import LabelAddMixin
from authors.models import Author


class AuthorBaseForm(LabelAddMixin, forms.ModelForm):
    image_label = 'Profile Image URL'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Author
        abstract = True
        fields = '__all__'


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...'
            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...'
            }),
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode']