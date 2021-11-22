from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from .forms import AgendasForm
from .forms import AgendasAlimentosForm
from .forms import AgendasBanhosForm
from .forms import AgendasFisiologiasForm
from .forms import AgendasItensForm
from .forms import AgendasMedicamentosForm
from .forms import AgendasRecadosForm
from .forms import AgendasSonosForm

from Cadastros.models import Agendas
from Cadastros.models import AgendasAlimentos
from Cadastros.models import AgendasBanhos
from Cadastros.models import AgendasFisiologias
from Cadastros.models import AgendasItens
from Cadastros.models import AgendasMedicamentos
from Cadastros.models import AgendasRecados
from Cadastros.models import AgendasSonos


def lista(request):
    if request.method == "GET":
        agendas = Agendas.objects.all()
        context = {
            "agendas": agendas,
        }
        return render(
            request, "Agenda/lista.html", context
        )  # Agenda/templates/Agenda/lista.html


def inserir(request):
    if request.method == "GET":
        AgendasMestre = AgendasForm()
        AlimentosFactory = inlineformset_factory(
            Agendas, AgendasAlimentos, form=AgendasAlimentosForm, extra=1
        )
        Alimentos = AlimentosFactory()
        BanhosFactory = inlineformset_factory(
            Agendas, AgendasBanhos, form=AgendasBanhosForm, extra=1
        )
        Banhos = BanhosFactory()
        FisiologiasFactory = inlineformset_factory(
            Agendas, AgendasFisiologias, form=AgendasFisiologiasForm, extra=1
        )
        Fisiologias = FisiologiasFactory()
        ItensFactory = inlineformset_factory(
            Agendas, AgendasItens, form=AgendasItensForm, extra=1
        )
        Itens = ItensFactory()
        MedicamentosFactory = inlineformset_factory(
            Agendas, AgendasMedicamentos, form=AgendasMedicamentosForm, extra=1
        )
        Medicamentos = MedicamentosFactory()
        RecadosFactory = inlineformset_factory(
            Agendas, AgendasRecados, form=AgendasRecadosForm, extra=1
        )
        Recados = RecadosFactory()
        SonosFactory = inlineformset_factory(
            Agendas, AgendasSonos, form=AgendasSonosForm, extra=1
        )
        Sonos = SonosFactory()
        context = {
            "Agendas": AgendasMestre,
            "Alimentos": Alimentos,
            "Banhos": Banhos,
            "Fisiologias": Fisiologias,
            "Itens": Itens,
            "Medicamentos": Medicamentos,
            "Recados": Recados,
            "Sonos": Sonos,
        }
        return render(request, "Agenda/form.html", context)
    elif request.method == "POST":
        AgendasMestre = AgendasForm(request.POST)
        AlimentosFactory = inlineformset_factory(
            Agendas, AgendasAlimentos, form=AgendasAlimentosForm
        )
        Alimentos = AlimentosFactory(request.POST)
        BanhosFactory = inlineformset_factory(
            Agendas, AgendasBanhos, form=AgendasBanhosForm
        )
        Banhos = BanhosFactory(request.POST)
        FisiologiasFactory = inlineformset_factory(
            Agendas, AgendasFisiologias, form=AgendasFisiologiasForm
        )
        Fisiologias = FisiologiasFactory(request.POST)
        ItensFactory = inlineformset_factory(
            Agendas, AgendasItens, form=AgendasItensForm
        )
        Itens = ItensFactory(request.POST)
        MedicamentosFactory = inlineformset_factory(
            Agendas, AgendasMedicamentos, form=AgendasMedicamentosForm
        )
        Medicamentos = MedicamentosFactory(request.POST)
        RecadosFactory = inlineformset_factory(
            Agendas, AgendasRecados, form=AgendasRecadosForm
        )
        Recados = RecadosFactory(request.POST)
        SonosFactory = inlineformset_factory(
            Agendas, AgendasSonos, form=AgendasSonosForm
        )
        Sonos = SonosFactory(request.POST)
        if AgendasMestre.is_valid():
            agenda = AgendasMestre.save()
            if Alimentos.is_valid():
                Alimentos.instance = agenda
                Alimentos.save()
            if Banhos.is_valid():
                Banhos.instance = agenda
                Banhos.save()
            if Fisiologias.is_valid():
                Fisiologias.instance = agenda
                Fisiologias.save()
            if Itens.is_valid():
                Itens.instance = agenda
                Itens.save()
            if Medicamentos.is_valid():
                Medicamentos.instance = agenda
                Medicamentos.save()
            if Recados.is_valid():
                Recados.instance = agenda
                Recados.save()
            if Sonos.is_valid():
                Sonos.instance = agenda
                Sonos.save()
            return redirect(reverse("agenda_lista"))
        else:
            context = {
                "Agendas": AgendasMestre,
                "Alimentos": Alimentos,
                "Banhos": Banhos,
                "Fisiologias": Fisiologias,
                "Itens": Itens,
                "Medicamentos": Medicamentos,
                "Recados": Recados,
                "Sonos": Sonos,
            }
            return render(request, "Agenda/form.html", context)


def editar(request, pk):
    if request.method == "GET":
        objeto = Agendas.objects.filter(Agenda_id=pk).first()
        if objeto is None:
            return redirect(reverse("agenda_lista"))
        AgendasMestre = AgendasForm(instance=objeto)
        AlimentosFactory = inlineformset_factory(
            Agendas, AgendasAlimentos, form=AgendasAlimentosForm, extra=1
        )
        Alimentos = AlimentosFactory(instance=objeto)
        BanhosFactory = inlineformset_factory(
            Agendas, AgendasBanhos, form=AgendasBanhosForm, extra=1
        )
        Banhos = BanhosFactory(instance=objeto)
        FisiologiasFactory = inlineformset_factory(
            Agendas, AgendasFisiologias, form=AgendasFisiologiasForm, extra=1
        )
        Fisiologias = FisiologiasFactory(instance=objeto)
        ItensFactory = inlineformset_factory(
            Agendas, AgendasItens, form=AgendasItensForm, extra=1
        )
        Itens = ItensFactory(instance=objeto)
        MedicamentosFactory = inlineformset_factory(
            Agendas, AgendasMedicamentos, form=AgendasMedicamentosForm, extra=1
        )
        Medicamentos = MedicamentosFactory(instance=objeto)
        RecadosFactory = inlineformset_factory(
            Agendas, AgendasRecados, form=AgendasRecadosForm, extra=1
        )
        Recados = RecadosFactory(instance=objeto)
        SonosFactory = inlineformset_factory(
            Agendas, AgendasSonos, form=AgendasSonosForm, extra=1
        )
        Sonos = SonosFactory(instance=objeto)
        context = {
            "Agendas": AgendasMestre,
            "Alimentos": Alimentos,
            "Banhos": Banhos,
            "Fisiologias": Fisiologias,
            "Itens": Itens,
            "Medicamentos": Medicamentos,
            "Recados": Recados,
            "Sonos": Sonos,
        }
        return render(request, "Agenda/form.html", context)
    elif request.method == "POST":
        objeto = Agendas.objects.filter(Agenda_id=pk).first()
        if objeto is None:
            return redirect(reverse("agenda_lista"))
        AgendasMestre = AgendasForm(request.POST, instance=objeto)
        AlimentosFactory = inlineformset_factory(
            Agendas, AgendasAlimentos, form=AgendasAlimentosForm
        )
        BanhosFactory = inlineformset_factory(
            Agendas, AgendasBanhos, form=AgendasBanhosForm
        )
        FisiologiasFactory = inlineformset_factory(
            Agendas, AgendasFisiologias, form=AgendasFisiologiasForm
        )
        ItensFactory = inlineformset_factory(
            Agendas, AgendasItens, form=AgendasItensForm
        )
        MedicamentosFactory = inlineformset_factory(
            Agendas, AgendasMedicamentos, form=AgendasMedicamentosForm
        )
        RecadosFactory = inlineformset_factory(
            Agendas, AgendasRecados, form=AgendasRecadosForm
        )
        SonosFactory = inlineformset_factory(
            Agendas, AgendasSonos, form=AgendasSonosForm
        )
        Alimentos = AlimentosFactory(request.POST, instance=objeto)
        Banhos = BanhosFactory(request.POST, instance=objeto)
        Fisiologias = FisiologiasFactory(request.POST, instance=objeto)
        Itens = ItensFactory(request.POST, instance=objeto)
        Medicamentos = MedicamentosFactory(request.POST, instance=objeto)
        Recados = RecadosFactory(request.POST, instance=objeto)
        Sonos = SonosFactory(request.POST, instance=objeto)
        if AgendasMestre.is_valid():
            agenda = AgendasMestre.save()
            if Alimentos.is_valid():
                Alimentos.instance = agenda
                Alimentos.save()
            if Banhos.is_valid():
                Banhos.instance = agenda
                Banhos.save()
            if Fisiologias.is_valid():
                Fisiologias.instance = agenda
                Fisiologias.save()
            if Itens.is_valid():
                Itens.instance = agenda
                Itens.save()
            if Medicamentos.is_valid():
                Medicamentos.instance = agenda
                Medicamentos.save()
            if Recados.is_valid():
                Recados.instance = agenda
                Recados.save()
            if Sonos.is_valid():
                Sonos.instance = agenda
                Sonos.save()
            return redirect(reverse("agenda_lista"))
        else:
            context = {
                "Agenda": AgendasMestre,
                "Alimentos": Alimentos,
                "Banhos": Banhos,
                "Fisiologias": Fisiologias,
                "Itens": Itens,
                "Medicamentos": Medicamentos,
                "Recados": Recados,
                "Sonos": Sonos,
            }
            return render(request, "Agenda/form.html", context)
