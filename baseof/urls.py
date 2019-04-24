from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('website.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('moduloof/', include('moduloof.urls')),
    path('modulopcp/', include('modulopcp.urls')),
]

