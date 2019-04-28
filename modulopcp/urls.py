from django.urls import path
from .views import Testeup, Upload_op


urlpatterns = [
    path('', Testeup.as_view(), name='url_testeimport'),
    path('upload-op/', Upload_op.as_view(), name='url_upload_op'),
]

