from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.

# Nivel 0 Alimentos
from .models import Alimentos


class AlimentosCreate(CreateView):
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosUpdate(UpdateView):
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosDelete(DeleteView):
    model = Alimentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alimentos-listar")


class AlimentosList(ListView):
    model = Alimentos
    template_name = "cadastros/listas/alimentos.html"


# Nivel 0 Itens
from .models import Itens


class ItensCreate(CreateView):
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensUpdate(UpdateView):
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensDelete(DeleteView):
    model = Itens
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("itens-listar")


class ItensList(ListView):
    model = Itens
    template_name = "cadastros/listas/itens.html"


# Nivel 0 Medicamentos
from .models import Medicamentos


class MedicamentosCreate(CreateView):
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosUpdate(UpdateView):
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosDelete(DeleteView):
    model = Medicamentos
    fields = ["Nome", "Descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("medicamentos-listar")


class MedicamentosList(ListView):
    model = Medicamentos
    template_name = "cadastros/listas/medicamentos.html"


# Nivel 0 Pessoas
from .models import Pessoas


class PessoasCreate(CreateView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pessoas-listar")


class PessoasUpdate(UpdateView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pessoas-listar")


class PessoasDelete(DeleteView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pessoas-listar")


class PessoasList(ListView):
    model = Pessoas
    template_name = "cadastros/listas/pessoas.html"


# Nivel 0 Turmas
from .models import Turmas


class TurmasCreate(CreateView):
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasUpdate(UpdateView):
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasDelete(DeleteView):
    model = Turmas
    fields = ["Nome", "AnoLetivo", "AnoEscolar"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class TurmasList(ListView):
    model = Turmas
    template_name = "cadastros/listas/turmas.html"


# Nivel 1 Alunos
from .models import Alunos


class AlunosCreate(CreateView):
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosUpdate(UpdateView):
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosDelete(DeleteView):
    model = Alunos
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("alunos-listar")


class AlunosList(ListView):
    model = Alunos
    template_name = "cadastros/listas/alunos.html"


# Nivel 1 Professores
from .models import Professores


class ProfessoresCreate(CreateView):
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresUpdate(UpdateView):
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresDelete(DeleteView):
    model = Professores
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("professores-listar")


class ProfessoresList(ListView):
    model = Professores
    template_name = "cadastros/listas/professores.html"


# Nivel 1 Responsaveis
from .models import Responsaveis


class ResponsaveisCreate(CreateView):
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisUpdate(UpdateView):
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisDelete(DeleteView):
    model = Responsaveis
    fields = ["Pessoa"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveis-listar")


class ResponsaveisList(ListView):
    model = Responsaveis
    template_name = "cadastros/listas/responsaveis.html"


# Nivel 2 ResponsaveisAlunos
from .models import ResponsaveisAlunos


class ResponsaveisAlunosCreate(CreateView):
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosUpdate(UpdateView):
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosDelete(DeleteView):
    model = ResponsaveisAlunos
    fields = ["Responsavel", "Aluno"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("responsaveisalunos-listar")


class ResponsaveisAlunosList(ListView):
    model = ResponsaveisAlunos
    template_name = "cadastros/listas/responsaveisalunos.html"
