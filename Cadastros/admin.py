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


# Nivel 3
from .models import Agendas
from .models import AgendasAlimentos
from .models import AgendasBanhos
from .models import AgendasFisiologias
from .models import AgendasItens
from .models import AgendasMedicamentos
from .models import AgendasRecados
from .models import AgendasSonos


class AgendaAlimentoInline(admin.StackedInline):
    model = AgendasAlimentos
    extra = 1


class AgendasBanhosInline(admin.StackedInline):
    model = AgendasBanhos
    extra = 1


class AgendasFisiologiasInline(admin.StackedInline):
    model = AgendasFisiologias
    extra = 1


class AgendasItensInline(admin.StackedInline):
    model = AgendasItens
    extra = 1


class AgendasMedicamentosInline(admin.StackedInline):
    model = AgendasMedicamentos
    extra = 1


class AgendasRecadosInline(admin.StackedInline):
    model = AgendasRecados
    extra = 1


class AgendasSonosInline(admin.StackedInline):
    model = AgendasSonos
    extra = 1


class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        AgendaAlimentoInline,
        AgendasBanhosInline,
        AgendasFisiologiasInline,
        AgendasItensInline,
        AgendasMedicamentosInline,
        AgendasRecadosInline,
        AgendasSonosInline,
    ]


admin.site.register(Agendas, AgendaAdmin)
