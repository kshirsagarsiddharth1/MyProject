from django.urls import path
from .controllers import AdditionController

urlpatterns = [
    path('add/', AdditionController.as_view(), name='add')
]
