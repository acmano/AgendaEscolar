from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.

# Nivel 0
# Alimentos
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


# Itens
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


# Medicamentos
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


# Pessoas
from .models import Pessoas


class PessoasCreate(CreateView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class PessoasUpdate(UpdateView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class PessoasDelete(DeleteView):
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("turmas-listar")


class PessoasList(ListView):
    model = Pessoas
    template_name = "cadastros/listas/turmas.html"


# Turmas
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
