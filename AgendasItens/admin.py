from django.contrib import admin
from .models import AgendasItens

# Register your models here.
@admin.register(AgendasItens)
class AgendasItensAdmin(admin.ModelAdmin):
    list_display = ["ItemId"]
