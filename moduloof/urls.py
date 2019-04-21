from django.urls import path
from .views import (
    Cadastro,
    Novo_ocadesivo,
    Locadesivo,
    duporcadesivo,
    cons_ocadesivo,
    Novo_ocfilme,
    duporcfilme,
    Locfilme,
    cons_ocfilme,
)

urlpatterns = [
    path('moduloof/cadastro/', Cadastro.as_view(),
         name='url_cadastro'),

    path('moduloof/locadesivo/', Locadesivo.as_view(),
         name='url_ladesivo'),
    path('moduloof/novoad/', Novo_ocadesivo.as_view(),
         name='url_novo_ocadesivo'),
    path('moduloof/duporcadesivo/<int:pk>/', duporcadesivo,
         name='url_duporcadesivo'),
    path('moduloof/consad/<int:pk>/', cons_ocadesivo,
         name='url_cons_ocadesivo'),

    path('moduloof/locfilme/', Locfilme.as_view(),
         name='url_lfilme'),
    path('moduloof/novofi/', Novo_ocfilme.as_view(),
         name='url_novo_ocfilme'),
    path('moduloof/duporcfilme/<int:pk>/', duporcfilme,
         name='url_duporcfilme'),
    path('moduloof/consfi/<int:pk>/', cons_ocfilme,
         name='url_cons_ocfilme'),
]
