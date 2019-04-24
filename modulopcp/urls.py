from django.urls import path
from .views import Import, uploadop


urlpatterns = [
    path('', Import.as_view(), name='url_import'),
    path('upload-csv/', uploadop, name='url_uploadop'),
]