from django.contrib import admin
from .models import ResponsaveisALunos

# Register your models here.
@admin.register(ResponsaveisALunos)
class ResponsaveisALunosAdmin(admin.ModelAdmin):
    list_display = ["ResponsavelId", "AlunoId"]
