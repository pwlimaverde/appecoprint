from django.urls import path
from .views import Upload_op, List_prod_comp_op, List_prod_op, Novo_reg_entrega


urlpatterns = [
    path('upload-op/', Upload_op.as_view(), name='url_upload_op'),
    path('list-prod-comp-op/', List_prod_comp_op.as_view(), name='url_list_prod_comp_op'),
    path('list-prod-op/', List_prod_op.as_view(), name='url_list_prod_op'),
    path('novo-entr-op/', Novo_reg_entrega.as_view(), name='url_novo_entr_op'),
]

