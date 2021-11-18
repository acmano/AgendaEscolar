from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.

# Nivel 0 Alimentos
from .models import Alimentos


class AlimentosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alimentos
    template_name = "cadastros/listas/alimentos.html"


# Nivel 0 Itens
from .models import Itens


class ItensCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Itens
    template_name = "cadastros/listas/itens.html"


# Nivel 0 Medicamentos
from .models import Medicamentos


class MedicamentosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Medicamentos
    template_name = "cadastros/listas/medicamentos.html"


# Nivel 0 Pessoas
from .models import Pessoas
from .forms import UserForm


class UserCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Convidados")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        Pessoas.objects.create(Usuario=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Registro de novo usuário"
        context["botao"] = "Cadastrar"
        return context


class PessoasUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "Telefone", "CPF", "RG"]
    success_url = reverse_lazy("atualizardados")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pessoas, Usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"
        return context


"""
    # Este código faz com que ocorra uma validação no UPDATE, permitindo somente ações feitas pelo próprio usuário cadastrado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pessoas, pk=self.kwargs['pk'], Usuario=self.request.user)
        return self.object
"""


# Nivel 0 Turmas
from .models import Turmas


class TurmasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Turmas
    template_name = "cadastros/listas/turmas.html"


# Nivel 1 Alunos
from .models import Alunos


class AlunosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Alunos
    template_name = "cadastros/listas/alunos.html"


# Nivel 1 Professores
from .models import Professores


class ProfessoresCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Professores
    template_name = "cadastros/listas/professores.html"


# Nivel 1 Responsaveis
from .models import Responsaveis


class ResponsaveisCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Responsaveis
    template_name = "cadastros/listas/responsaveis.html"


# Nivel 2 ResponsaveisAlunos
from .models import ResponsaveisAlunos


class ResponsaveisAlunosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = ResponsaveisAlunos
    template_name = "cadastros/listas/responsaveisalunos.html"


# Nivel 2 Matriculas
from .models import Matriculas


class MatriculasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Matriculas
    fields = ["Turma", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("matriculas-listar")


class MatriculasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Matriculas
    fields = ["Turma", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("matriculas-listar")


class MatriculasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Matriculas
    fields = ["Turma", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("matriculas-listar")


class MatriculasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Matriculas
    template_name = "cadastros/listas/matriculas.html"


# Nivel 2 Matriculas
from .models import TurmasProfessores


class TurmasProfessoresCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    template_name = "cadastros/listas/turmasprofessores.html"


# Nivel 2 TurmasProfessores
from .models import TurmasProfessores


class TurmasProfessoresCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    fields = ["Turma", "Professor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmasprofessores-listar")


class TurmasProfessoresList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = TurmasProfessores
    template_name = "cadastros/listas/turmasprofessores.html"


# Nivel 2 Prescricoes
from .models import Prescricoes


class PrescricoesCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Prescricoes
    fields = [
        "Alunos",
        "Medicamento",
        "DataInicial",
        "DataFinal",
        "Posologia",
        "Horarios",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("prescricoes-listar")


class PrescricoesUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Prescricoes
    fields = [
        "Alunos",
        "Medicamento",
        "DataInicial",
        "DataFinal",
        "Posologia",
        "Horarios",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("prescricoes-listar")


class PrescricoesDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Prescricoes
    fields = [
        "Alunos",
        "Medicamento",
        "DataInicial",
        "DataFinal",
        "Posologia",
        "Horarios",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("prescricoes-listar")


class PrescricoesList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Prescricoes
    template_name = "cadastros/listas/prescricoes.html"


# Nivel 3 Agendas
from .models import Agendas


class AgendasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Agendas
    fields = ["TurmaProfessor", "Matricula", "Data"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("agendas-listar")


class AgendasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Agendas
    fields = ["TurmaProfessor", "Matricula", "Data"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("agendas-listar")


class AgendasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Agendas
    fields = ["TurmaProfessor", "Matricula", "Data"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("agendas-listar")


class AgendasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    group_required = [u"", u""]
    model = Agendas
    template_name = "cadastros/listas/Agendas.html"


# Nivel 2 Prescricoes
from .forms import AgendaForm

# class AgendaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
class AgendaCreate(CreateView):
    template_name = "cadastros/listas/agenda.html"
    form_class = AgendaForm
    success_url = reverse_lazy("agenda-dados")

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")


