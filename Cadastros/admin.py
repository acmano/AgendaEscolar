from django.contrib import admin

# Register your models here.
# Nivel 0
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

# Nivel 1
from .models import Alunos
from .models import Professores
from .models import Responsaveis

admin.site.register(Alunos)
admin.site.register(Professores)
admin.site.register(Responsaveis)

# Nivel 2
from .models import ResponsaveisAlunos
from .models import Matriculas
from .models import TurmasProfessores
from .models import Prescricoes

admin.site.register(ResponsaveisAlunos)
admin.site.register(Matriculas)
admin.site.register(TurmasProfessores)
admin.site.register(Prescricoes)
