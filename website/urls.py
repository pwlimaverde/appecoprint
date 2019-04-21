from django.urls import path
from .views import Home_website


urlpatterns = [
    path('', Home_website.as_view(), name='url_home_website'),
]