from django.contrib import admin
from .models import Professores

# Register your models here.
@admin.register(Professores)
class ProfessoresAdmin(admin.ModelAdmin):
    list_display = ["ProfessorId"]
