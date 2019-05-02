from django.urls import path
from .views import Upload_op, List_prod_comp_op, List_prod_op, List_ent_op, upprod, upent


urlpatterns = [
    path('upload-op/', Upload_op.as_view(),
         name='url_upload_op'),
    path('list-prod-comp-op/', List_prod_comp_op.as_view(),
         name='url_list_prod_comp_op'),
    path('list-prod-op/', List_prod_op.as_view(),
         name='url_list_prod_op'),
    path('list-ent-op/', List_ent_op.as_view(),
         name='url_list_ent_op'),
    path('list-prod-op/<int:pk>/', upprod,
         name='url_list_prod_up_op'),
    path('list-ent-op/<int:pk>/', upent,
         name='url_list_ent_up_op'),
]

