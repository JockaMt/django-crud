from django.urls import path
from .views import list_motos, create_motos

urlpatterns = [
    path('', list_motos, name='list_motos'),
    path('new', create_motos, name='create_motos'),
]