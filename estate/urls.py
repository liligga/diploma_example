from django.urls import path
from .views import house_create, detail_create, house_list, image_create


urlpatterns = [
    path('', house_list, name='house_list'),
    path('houses/new', house_create, name='house_create'),   
    path('<house_id>/details/new', detail_create, name='detail_create'),   
    path('<house_id>/images/new', image_create, name='image_create'),   
]