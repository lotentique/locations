from django.urls import path
from .import views
app_name='voitures'
urlpatterns = [
    path('',views.index,name='acceuil'),
    path('mesvoitures/',views.voitures,name='mesvoitures'),
    path('locations/',views.locations,name='locations'),
    path('client',views.client,name='client'),
]