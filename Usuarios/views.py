from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from Cadastros.models import Pessoas

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "Cadastros/form.html"
    form_class = UsuarioForm
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


class PessoaUpdate(UpdateView):
    template_name = "Cadastros/form.html"
    model = Pessoas
    fields = ["Nome", "Apelido", "DataNascimento", "Telefone", "CPF", "RG"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pessoas, Usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"
        return context
