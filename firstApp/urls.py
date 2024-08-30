from firstApp.views import display
from firstApp.views import displayDateTime
from django.urls import path

urlpatterns = [
    path('hola/', display)
]