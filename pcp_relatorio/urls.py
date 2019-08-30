from django.urls import path
from .views import (
    Impprod,
    Impexped,
    Pdfprod,
    Pdfexped,
)


urlpatterns = [
    path('impprop/', Impprod.as_view(),
         name='impprop'),
    path('impexped/', Impexped.as_view(),
         name='impexped'),

    path('rel-prod-op/', Pdfprod.as_view(),
         name='url_rel_prod_op'),
    path('rel-exped-op/', Pdfexped.as_view(),
         name='url_rel_exped_op'),
]
