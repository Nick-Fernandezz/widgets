from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='index_page'),
    path('weather/', weather_page, name='weather_page'),
    path('exchange/', exchange_page, name='exchange_page')
]
