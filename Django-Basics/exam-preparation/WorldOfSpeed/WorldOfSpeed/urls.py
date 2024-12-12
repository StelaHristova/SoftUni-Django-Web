
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('car/', include('car.urls')),
    path('profile/', include('profiles.urls'))
]
