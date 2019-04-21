from django.urls import path
from .views import (
    Cadastro,
    Novo_ocadesivo,
    Dupocadesivo,
    Delocadesivo,
    Locadesivo,
    Cons_ocadesivo,
    Novo_ocfilme,
    Dupocfilme,
    Delocfilme,
    Locfilme,
    Cons_ocfilme,
)

urlpatterns = [
    path('moduloof/cadastro/', Cadastro.as_view(),
         name='url_cadastro'),

    path('moduloof/locadesivo/', Locadesivo.as_view(),
         name='url_ladesivo'),
    path('moduloof/novoad/', Novo_ocadesivo.as_view(),
         name='url_novo_ocadesivo'),
    path('moduloof/dupad/<int:pk>/', Dupocadesivo.as_view(),
         name='url_dup_ocadesivo'),
    path('moduloof/delad/<int:pk>/', Delocadesivo.as_view(),
         name='url_del_ocadesivo'),
    path('moduloof/consad/<int:pk>/', Cons_ocadesivo.as_view(),
         name='url_cons_ocadesivo'),

    path('moduloof/locfilme/', Locfilme.as_view(),
         name='url_lfilme'),
    path('moduloof/novofi/', Novo_ocfilme.as_view(),
         name='url_novo_ocfilme'),
    path('moduloof/dupfi/<int:pk>/', Dupocfilme.as_view(),
         name='url_dup_ocfilme'),
    path('moduloof/delfi/<int:pk>/', Delocfilme.as_view(),
         name='url_del_ocfilme'),
    path('moduloof/consfi/<int:pk>/', Cons_ocfilme.as_view(),
         name='url_cons_ocfilme'),
]
