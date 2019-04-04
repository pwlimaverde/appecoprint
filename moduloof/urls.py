from django.urls import path
from .views import (
    home,
    locadesivo,
    novo_ocadesivo,
    cons_ocadesivo,
    novo_ocfilme,
    locfilme,
    cons_ocfilme,
    lorc_adesivo,
    novo_orc_adesivo,
    cons_orc_adesivo
)

urlpatterns = [
    path('', home,
         name='url_home'),

    path('moduloof/locadesivo/', locadesivo,
         name='url_ladesivo'),
    path('moduloof/novoad/', novo_ocadesivo,
         name='url_novo_ocadesivo'),
    path('moduloof/consad/<int:pk>/', cons_ocadesivo,
         name='url_cons_ocadesivo'),

    path('moduloof/lorc_adesivo/', lorc_adesivo,
         name='url_lorc_adesivo'),
    path('moduloof/novo_orc_ad/', novo_orc_adesivo,
         name='url_novo_orc_adesivo'),
    path('moduloof/cons_orc_ad/<int:pk>/', cons_orc_adesivo,
         name='url_cons_orc_adesivo'),

    path('moduloof/locfilme/', locfilme,
         name='url_lfilme'),
    path('moduloof/novofi/', novo_ocfilme,
         name='url_novo_ocfilme'),
    path('moduloof/consfi/<int:pk>/', cons_ocfilme,
         name='url_cons_ocfilme'),
]

