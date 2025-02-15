from django.urls import path
from common import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index-page'),
    path('all-trips/', views.AllTripsView.as_view(), name='all-trips')
]