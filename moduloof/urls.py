from django.urls import path
from .views import (
    cadastro,
    locadesivo,
    novo_ocadesivo,
    duporcadesivo,
    cons_ocadesivo,
    novo_ocfilme,
    duporcfilme,
    locfilme,
    cons_ocfilme,
)

urlpatterns = [
    path('moduloof/cadastro/', cadastro,
         name='url_cadastro'),

    path('moduloof/locadesivo/', locadesivo,
         name='url_ladesivo'),
    path('moduloof/novoad/', novo_ocadesivo,
         name='url_novo_ocadesivo'),
    path('moduloof/duporcadesivo/<int:pk>/', duporcadesivo,
         name='url_duporcadesivo'),
    path('moduloof/consad/<int:pk>/', cons_ocadesivo,
         name='url_cons_ocadesivo'),

    path('moduloof/locfilme/', locfilme,
         name='url_lfilme'),
    path('moduloof/novofi/', novo_ocfilme,
         name='url_novo_ocfilme'),
    path('moduloof/duporcfilme/<int:pk>/', duporcfilme,
         name='url_duporcfilme'),
    path('moduloof/consfi/<int:pk>/', cons_ocfilme,
         name='url_cons_ocfilme'),
]
