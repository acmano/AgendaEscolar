from django.contrib import admin
from .models import AgendasFisiologias

# Register your models here.
@admin.register(AgendasFisiologias)
class AgendasFisiologiasAdmin(admin.ModelAdmin):
    list_display = ["Hora", "Tipo"]
