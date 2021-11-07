from django.contrib import admin
from .models import Alimentos

# Register your models here.
@admin.register(Alimentos)
class AlimentosAdmin(admin.ModelAdmin):
    list_display = ["Nome"]
