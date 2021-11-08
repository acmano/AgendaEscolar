from django.contrib import admin
from .models import AgendasRecados

# Register your models here.
@admin.register(AgendasRecados)
class AgendasRecadosAdmin(admin.ModelAdmin):
    list_display = ["Recado"]
