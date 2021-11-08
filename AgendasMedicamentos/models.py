from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class AgendasMedicamentos(models.Model):
    AgendaMedicamentoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaMedicamentoId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasMedicamentosAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    PrescricaoId = models.ForeignKey(
        "Prescricoes.Prescricoes",
        related_name="AgendasMedicamentosPrescricoes",
        verbose_name="Medicamento",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Hora = models.TimeField(verbose_name="Hora", blank=False, null=False)
    PosologiaAdministrada = models.CharField(max_length=50, blank=False, null=False)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="AgendaMedicamentoId"
    )

    class Meta:
        db_table = "AgendasMedicamentos"
        verbose_name = "AgendaMedicamento"
        verbose_name_plural = "AgendasAMedicamentos"
        unique_together = ("AgendaId", "PrescricaoId", "Hora")
        UniqueConstraint(fields=["AgendaMedicamentoId"], name="AgendaMedicamentoPK")
        UniqueConstraint(
            fields=["AgendaId", "PrescricaoId", "Hora"], name="AgendaMedicamentoAK"
        )

    def __str__(self):
        return str(self.AgendaMedicamentoId)

    def get_absolute_url(self):
        return reverse(
            "AgendasMedicamentos:AgendasMedicamentos", kwargs={"slug": self.slug}
        )
