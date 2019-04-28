from django.urls import path
from .views import testeup


urlpatterns = [
    path('', testeup, name='url_Testeimport'),
]

