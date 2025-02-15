from django.urls import path, include

from trips import views

urlpatterns = [
    path('create/', views.TripCreateView.as_view(), name='trip-create'),
    path('<int:trip_pk>/details/', views.TripDetailsView.as_view(), name='trip-details'),
    path('<int:trip_pk>/edit/', views.TripEditView.as_view(), name='trip-edit'),
    path('<int:trip_pk>/delete/', views.TripDeleteView.as_view(), name='trip-delete'),
]