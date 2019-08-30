from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('website.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('moduloof/', include('moduloof.urls')),
    path('pcp_upload_xls/', include('pcp_upload_xls.urls')),
    path('pcp_relatorio/', include('pcp_relatorio.urls')),
    path('pcp_registro_entrega/', include('pcp_registro_entrega.urls')),
]

