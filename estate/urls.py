from django.urls import path
from .views import house_create


urlpatterns = [
    path('', house_create, name='house_create')    
]