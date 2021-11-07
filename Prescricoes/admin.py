from django.contrib import admin
from .models import Prescricoes

# Register your models here.
@admin.register(Prescricoes)
class PrescricoesAdmin(admin.ModelAdmin):
    list_display = [
        "MedicamentoId",
        "AlunoId",
        "DataInicio",
        "DataFim",
        "Posologia",
        "Horarios",
    ]
