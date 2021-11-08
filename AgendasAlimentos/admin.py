from django.contrib import admin
from .models import AgendasAlimentos

# Register your models here.
@admin.register(AgendasAlimentos)
class AgendasAlimentosAdmin(admin.ModelAdmin):
    list_display = ["Hora", "AlimentoId", "Aceite"]
