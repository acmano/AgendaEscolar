from django.contrib import admin

# Register your models here.
from Cadastros.models import *

class AgendaAlimentoInline(admin.StackedInline):
    model = AgendasAlimentos
    
class AgendaAdmin(admin.ModelAdmin):
    inlines=[
      AgendasAlimentos
    ]