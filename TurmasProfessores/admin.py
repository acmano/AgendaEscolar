from django.contrib import admin
from .models import TurmasProfessores

# Register your models here.
@admin.register(TurmasProfessores)
class TurmasProfessoresAdmin(admin.ModelAdmin):
    list_display = ["TurmaId", "ProfessorId"]
