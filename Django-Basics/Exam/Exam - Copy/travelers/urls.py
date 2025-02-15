from django.urls import path

from travelers import views

urlpatterns = [
    path('create/', views.TravelerCreateView.as_view(), name='traveler-create'),
    path('details/', views.TravelerDetailsView.as_view(), name='traveler-details'),
    path('edit/', views.TravelerEditView.as_view(), name='traveler-edit'),
    path('delete/', views.TravelerDeleteView.as_view(), name='traveler-delete'),
]