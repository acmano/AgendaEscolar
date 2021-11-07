from django.contrib import admin
from .models import Responsaveis

# Register your models here.
@admin.register(Responsaveis)
class ResponsaveisAdmin(admin.ModelAdmin):
    list_display = ["PessoaId"]
