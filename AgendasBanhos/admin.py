from django.contrib import admin
from .models import AgendasBanhos

# Register your models here.
@admin.register(AgendasBanhos)
class AgendasBanhosAdmin(admin.ModelAdmin):
    list_display = ["Hora"]
