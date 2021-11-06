from django.contrib import admin
from .models import Pessoas

# Register your models here.
@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ["Nome", "Apelido", "DataNascimento", "CPF", "RG", "EMail", "Senha"]
