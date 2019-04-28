from django.urls import path
from .views import Upload_op


urlpatterns = [
    path('upload-op/', Upload_op.as_view(), name='url_upload_op'),
]

