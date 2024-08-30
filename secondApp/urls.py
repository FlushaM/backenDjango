from secondApp.views import display
from django.urls import path

urlpatterns = [
    path('saludo/', display)
]