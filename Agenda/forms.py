from django import forms

from Cadastros.models import Agendas
from Cadastros.models import AgendasAlimentos
from Cadastros.models import AgendasBanhos
from Cadastros.models import AgendasFisiologias
from Cadastros.models import AgendasItens
from Cadastros.models import AgendasMedicamentos
from Cadastros.models import AgendasRecados
from Cadastros.models import AgendasSonos


class AgendasForm(forms.ModelForm):
    class Meta:
        model = Agendas
        fields = ["TurmaProfessor", "Matricula", "Data"]


class AgendasAlimentosForm(forms.ModelForm):
    class Meta:
        model = AgendasAlimentos
        fields = ["Hora", "Alimento", "Aceite"]


class AgendasBanhosForm(forms.ModelForm):
    class Meta:
        model = AgendasBanhos
        fields = ["Hora"]


class AgendasFisiologiasForm(forms.ModelForm):
    class Meta:
        model = AgendasFisiologias
        fields = ["Hora", "Fisiologia"]


class AgendasItensForm(forms.ModelForm):
    class Meta:
        model = AgendasItens
        fields = ["Item"]


class AgendasMedicamentosForm(forms.ModelForm):
    class Meta:
        model = AgendasMedicamentos
        fields = ["Hora", "Prescricao", "PosologiaAdministrada"]


class AgendasRecadosForm(forms.ModelForm):
    class Meta:
        model = AgendasRecados
        fields = ["Recado"]


class AgendasSonosForm(forms.ModelForm):
    class Meta:
        model = AgendasSonos
        fields = ["Inicio", "Fim"]
