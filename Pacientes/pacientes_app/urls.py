#from django.conf.urls import urls
from django.urls import path, include
from .views import (
    PacienteListApiView,
)

urlpatterns = [
    path('api', PacienteListApiView.as_view()),
]