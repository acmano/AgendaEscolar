from django.contrib import admin
from .models import Alunos

# Register your models here.
@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ["AlunoId"]
