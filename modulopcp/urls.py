from django.urls import path
from .views import Testeup


urlpatterns = [
    path('', Testeup.as_view(), name='url_Testeimport'),
]