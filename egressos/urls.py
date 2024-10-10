from django.urls import path
from egressos.views import index

urlpatterns = [
    path('', index),
]