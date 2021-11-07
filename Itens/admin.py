from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Itens

# Register your models here.
@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ["Nome"]
