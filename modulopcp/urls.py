from django.urls import path
from .views import Upload_op, List_prod_comp_op, List_prod_op, upcancelada


urlpatterns = [
    path('upload-op/', Upload_op.as_view(), name='url_upload_op'),
    path('list-prod-comp-op/', List_prod_comp_op.as_view(), name='url_list_prod_comp_op'),
    path('list-prod-op/', List_prod_op.as_view(), name='url_list_prod_op'),
    path('list-prod-comp-op/<int:pk>/', upcancelada,
         name='url_list_prod_comp_up_op'),
]

