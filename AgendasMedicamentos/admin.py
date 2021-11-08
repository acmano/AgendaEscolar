from django.contrib import admin
from .models import AgendasMedicamentos

# Register your models here.
@admin.register(AgendasMedicamentos)
class AgendasMedicamentosAdmin(admin.ModelAdmin):
    list_display = ["Hora", "PrescricaoId", "PosologiaAdministrada"]
