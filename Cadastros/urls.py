"""Progressao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Nivel 0 - ALimentos
from django.urls import path
from .views import AlimentosCreate
from .views import AlimentosUpdate
from .views import AlimentosDelete
from .views import AlimentosList


urlpatterns = [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("alimento/cadastrar/", AlimentosCreate.as_view(), name="alimento-cadastrar"),
    path(
        "alimento/editar/<int:pk>/", AlimentosUpdate.as_view(), name="alimento-editar"
    ),
    path(
        "alimento/excluir/<int:pk>/",
        AlimentosDelete.as_view(),
        name="alimento-excluir",
    ),
    path("alimentos/listar/", AlimentosList.as_view(), name="alimentos-listar"),
]

from .views import ItensCreate
from .views import ItensUpdate
from .views import ItensDelete
from .views import ItensList

# Nivel 0 - Itens
urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("item/cadastrar/", ItensCreate.as_view(), name="item-cadastrar"),
    path("item/editar/<int:pk>/", ItensUpdate.as_view(), name="item-editar"),
    path("item/excluir/<int:pk>/", ItensDelete.as_view(), name="item-excluir"),
    path("itens/listar/", ItensList.as_view(), name="itens-listar"),
]

# Nivel 0 - Medicamentos
from .views import MedicamentosCreate
from .views import MedicamentosUpdate
from .views import MedicamentosDelete
from .views import MedicamentosList


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "medicamento/cadastrar/",
        MedicamentosCreate.as_view(),
        name="medicamento-cadastrar",
    ),
    path(
        "medicamento/editar/<int:pk>/",
        MedicamentosUpdate.as_view(),
        name="medicamento-editar",
    ),
    path(
        "medicamento/excluir/<int:pk>/",
        MedicamentosDelete.as_view(),
        name="medicamento-excluir",
    ),
    path(
        "medicamentos/listar/", MedicamentosList.as_view(), name="medicamentos-listar"
    ),
]

# Nivel 0 - Pessoas
from .views import PessoasCreate
from .views import PessoasUpdate
from .views import PessoasDelete
from .views import PessoasList


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("pessoa/cadastrar/", PessoasCreate.as_view(), name="pessoa-cadastrar"),
    path("pessoa/editar/<int:pk>/", PessoasUpdate.as_view(), name="pessoa-editar"),
    path("pessoa/excluir/<int:pk>/", PessoasDelete.as_view(), name="pessoa-excluir"),
    path("pessoas/listar/", PessoasList.as_view(), name="pessoas-listar"),
]

# Nivel 0 - Turmas
from .views import TurmasCreate
from .views import TurmasUpdate
from .views import TurmasDelete
from .views import TurmasList


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("turma/cadastrar/", TurmasCreate.as_view(), name="turma-cadastrar"),
    path("turma/editar/<int:pk>/", TurmasUpdate.as_view(), name="turma-editar"),
    path("turma/excluir/<int:pk>/", TurmasDelete.as_view(), name="turma-excluir"),
    path("turmas/listar/", TurmasList.as_view(), name="turmas-listar"),
]
