from django.contrib import admin
from .models import Agendas

# Register your models here.
@admin.register(Agendas)
class AgendasAdmin(admin.ModelAdmin):
    list_display = ["MatriculaId", "TurmaProfessorId", "Data"]
