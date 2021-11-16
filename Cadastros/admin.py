from django.contrib import admin

# Register your models here.
from .models import Alimentos
from .models import Itens
from .models import Medicamentos
from .models import Pessoas
from .models import Turmas

admin.site.register(Alimentos)
admin.site.register(Itens)
admin.site.register(Medicamentos)
admin.site.register(Pessoas)
admin.site.register(Turmas)
