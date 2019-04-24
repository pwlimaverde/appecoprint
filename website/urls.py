from django.urls import path
from .views import Home_website,uploadop


urlpatterns = [
    path('', Home_website.as_view(), name='url_home_website'),
    path('upload-csv/', uploadop, name='url_uploadop'),
]