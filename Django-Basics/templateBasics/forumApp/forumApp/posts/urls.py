from django.urls import path

from forumApp.posts.views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
]