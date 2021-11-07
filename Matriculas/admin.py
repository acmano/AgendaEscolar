from django.contrib import admin
from .models import Matriculas

# Register your models here.
@admin.register(Matriculas)
class MatriculasAdmin(admin.ModelAdmin):
    list_display = ["TurmaId", "AlunoId"]
