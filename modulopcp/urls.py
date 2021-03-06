from django.urls import path
from .views import (
    Upload_op,
    List_prod_comp_op,
    List_prod_op,
    Pdfprod,
    List_ent_op,
    Pdfexped,
    upprod,
    canprod,
    upent,
    Impprod,
    Impexped,
)


urlpatterns = [
    path('impprop/', Impprod.as_view(),
         name='impprop'),
    path('impexped/', Impexped.as_view(),
         name='impexped'),

    path('upload-op/', Upload_op.as_view(),
         name='url_upload_op'),
    path('list-prod-comp-op/', List_prod_comp_op.as_view(),
         name='url_list_prod_comp_op'),
    path('list-prod-op/', List_prod_op.as_view(),
         name='url_list_prod_op'),
    path('rel-prod-op/', Pdfprod.as_view(),
         name='url_rel_prod_op'),
    path('list-ent-op/', List_ent_op.as_view(),
         name='url_list_ent_op'),
    path('rel-exped-op/', Pdfexped.as_view(),
         name='url_rel_exped_op'),
    path('list-prod-up-op/<int:pk>', upprod,
         name='url_list_prod_up_op'),
    path('list-prod-can-op/<int:pk>', canprod,
         name='url_list_prod_can_op'),
    path('list-ent-up-op/<int:pk>/', upent,
         name='url_list_ent_up_op'),
]

