from django.urls import path
from .views import home_website


urlpatterns = [
    path('', home_website, name='url_home_website'),
]