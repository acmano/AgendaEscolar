"""
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
"""
from django.contrib.auth import views as auth_views
from django.urls import path

# Nivel 0 - ALimentos
from .views import AlimentosCreate, AlimentosUpdate, AlimentosDelete, AlimentosList
from .views import ItensCreate, ItensUpdate, ItensDelete, ItensList
from .views import (
    MedicamentosCreate,
    MedicamentosUpdate,
    MedicamentosDelete,
    MedicamentosList,
)
from .views import TurmasCreate, TurmasUpdate, TurmasDelete, TurmasList
from .views import AlunosCreate, AlunosUpdate, AlunosDelete, AlunosList
from .views import (
    ProfessoresCreate,
    ProfessoresUpdate,
    ProfessoresDelete,
    ProfessoresList,
)
from .views import (
    ResponsaveisCreate,
    ResponsaveisUpdate,
    ResponsaveisDelete,
    ResponsaveisList,
)
from .views import (
    ResponsaveisAlunosCreate,
    ResponsaveisAlunosUpdate,
    ResponsaveisAlunosDelete,
    ResponsaveisAlunosList,
)
from .views import MatriculasCreate, MatriculasUpdate, MatriculasDelete, MatriculasList
from .views import (
    TurmasProfessoresCreate,
    TurmasProfessoresUpdate,
    TurmasProfessoresDelete,
    TurmasProfessoresList,
)
from .views import (
    PrescricoesCreate,
    PrescricoesUpdate,
    PrescricoesDelete,
    PrescricoesList,
)
from .views import AgendasCreate, AgendasUpdate, AgendasDelete, AgendasList
from .views import UserCreate, PessoasUpdate, AgendaCreate, PasswordsChangeView


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

# Nivel 0 - Itens
urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("item/cadastrar/", ItensCreate.as_view(), name="item-cadastrar"),
    path("item/editar/<int:pk>/", ItensUpdate.as_view(), name="item-editar"),
    path("item/excluir/<int:pk>/", ItensDelete.as_view(), name="item-excluir"),
    path("itens/listar/", ItensList.as_view(), name="itens-listar"),
]

# Nivel 0 - Medicamentos


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


# Nivel 0 - Turmas


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("turma/cadastrar/", TurmasCreate.as_view(), name="turma-cadastrar"),
    path("turma/editar/<int:pk>/", TurmasUpdate.as_view(), name="turma-editar"),
    path("turma/excluir/<int:pk>/", TurmasDelete.as_view(), name="turma-excluir"),
    path("turmas/listar/", TurmasList.as_view(), name="turmas-listar"),
]


# Nivel 1 - Alunos


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path("aluno/cadastrar/", AlunosCreate.as_view(), name="aluno-cadastrar"),
    path("aluno/editar/<int:pk>/", AlunosUpdate.as_view(), name="aluno-editar"),
    path("aluno/excluir/<int:pk>/", AlunosDelete.as_view(), name="aluno-excluir"),
    path("alunos/listar/", AlunosList.as_view(), name="alunos-listar"),
]


# Nivel 1 - Professores


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "professor/cadastrar/", ProfessoresCreate.as_view(), name="professor-cadastrar"
    ),
    path(
        "professor/editar/<int:pk>/",
        ProfessoresUpdate.as_view(),
        name="professor-editar",
    ),
    path(
        "professor/excluir/<int:pk>/",
        ProfessoresDelete.as_view(),
        name="professor-excluir",
    ),
    path("professor/listar/", ProfessoresList.as_view(), name="professores-listar"),
]


# Nivel 1 - Responsaveis


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "responsavel/cadastrar/",
        ResponsaveisCreate.as_view(),
        name="responsavel-cadastrar",
    ),
    path(
        "responsavel/editar/<int:pk>/",
        ResponsaveisUpdate.as_view(),
        name="responsavel-editar",
    ),
    path(
        "responsavel/excluir/<int:pk>/",
        ResponsaveisDelete.as_view(),
        name="responsavel-excluir",
    ),
    path("responsavel/listar/", ResponsaveisList.as_view(), name="responsaveis-listar"),
]


# Nivel 2 - ResponsaveisAlunos


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "responsavelaluno/cadastrar/",
        ResponsaveisAlunosCreate.as_view(),
        name="responsavelaluno-cadastrar",
    ),
    path(
        "responsavelaluno/editar/<int:pk>/",
        ResponsaveisAlunosUpdate.as_view(),
        name="responsavelaluno-editar",
    ),
    path(
        "responsavelaluno/excluir/<int:pk>/",
        ResponsaveisAlunosDelete.as_view(),
        name="responsavelaluno-excluir",
    ),
    path(
        "responsavelaluno/listar/",
        ResponsaveisAlunosList.as_view(),
        name="responsaveisalunos-listar",
    ),
]


# Nivel 2 - Matriculas


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "matricula/cadastrar/",
        MatriculasCreate.as_view(),
        name="matricula-cadastrar",
    ),
    path(
        "matricula/editar/<int:pk>/",
        MatriculasUpdate.as_view(),
        name="matricula-editar",
    ),
    path(
        "matricula/excluir/<int:pk>/",
        MatriculasDelete.as_view(),
        name="matricula-excluir",
    ),
    path(
        "matricula/listar/",
        MatriculasList.as_view(),
        name="matriculas-listar",
    ),
]


# Nivel 2 - TurmasProfessores


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "turmaprofessor/cadastrar/",
        TurmasProfessoresCreate.as_view(),
        name="turmaprofessor-cadastrar",
    ),
    path(
        "turmaprofessor/editar/<int:pk>/",
        TurmasProfessoresUpdate.as_view(),
        name="turmaprofessor-editar",
    ),
    path(
        "turmaprofessor/excluir/<int:pk>/",
        TurmasProfessoresDelete.as_view(),
        name="turmaprofessor-excluir",
    ),
    path(
        "turmaprofessor/listar/",
        TurmasProfessoresList.as_view(),
        name="turmasprofessores-listar",
    ),
]


# Nivel 2 - Prescricoes


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "prescricao/cadastrar/",
        PrescricoesCreate.as_view(),
        name="prescricao-cadastrar",
    ),
    path(
        "prescricao/editar/<int:pk>/",
        PrescricoesUpdate.as_view(),
        name="prescricao-editar",
    ),
    path(
        "prescricao/excluir/<int:pk>/",
        PrescricoesDelete.as_view(),
        name="prescricao-excluir",
    ),
    path(
        "prescricoes/listar/",
        PrescricoesList.as_view(),
        name="prescricoes-listar",
    ),
]


# Nivel 3 - Agendas


urlpatterns += [
    #   path("endereco/", MinhaView.as_view(), name="endereco"),
    path(
        "agenda/cadastrar/",
        AgendasCreate.as_view(),
        name="agenda-cadastrar",
    ),
    path(
        "agenda/editar/<int:pk>/",
        AgendasUpdate.as_view(),
        name="agenda-editar",
    ),
    path(
        "agenda/excluir/<int:pk>/",
        AgendasDelete.as_view(),
        name="agenda-excluir",
    ),
    path(
        "agenda/listar/",
        AgendasList.as_view(),
        name="agendas-listar",
    ),
]


# Usuarios

urlpatterns += [
    # path("endereco/", MinhaView.as_view(), name="endereco"),
    # path("login/",auth_views.LoginView.as_view(template_name="paginas/login.html"),name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("registrar/", UserCreate.as_view(), name="registrar"),
    path("atualizardados/", PessoasUpdate.as_view(), name="atualizardados"),
    path("agenda/dados/", AgendaCreate.as_view(), name="agenda-dados"),
    # path("password/",PasswordsChangeView.as_view(template_name="paginas/password.html"),name="password",),
]
