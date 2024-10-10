from django.contrib import admin
from django.urls import path, include

"""

Todas as URLs do egresu

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('egressos.urls')),
]
