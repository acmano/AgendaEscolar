from django.contrib import admin
from .models import Turmas

# Register your models here.
@admin.register(Turmas)
class TurmasAdmin(admin.ModelAdmin):
    list_display = ["Nome", "AnoLetivo", "AnoEscolar"]
