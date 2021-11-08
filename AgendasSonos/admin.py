from django.contrib import admin
from .models import AgendasSonos

# Register your models here.
@admin.register(AgendasSonos)
class AgendasSonosAdmin(admin.ModelAdmin):
    list_display = ["Inicio", "Fim"]
