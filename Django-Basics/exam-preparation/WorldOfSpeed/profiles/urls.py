from django.urls import path, include

from profiles.views import CreateProfile, ProfileDetails, ProfileEdit, ProfileDelete

urlpatterns = [
    path('', include([
        path('create/', CreateProfile.as_view(), name='profile create'),
        path('details/', ProfileDetails.as_view() ,name='profile details'),
        path('edit/', ProfileEdit.as_view() ,name='profile edit'),
        path('delete/', ProfileDelete.as_view() ,name='profile delete'),
    ]))
]