from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class AgendasRecados(models.Model):
    AgendaRecadoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaRecadoId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasRecadosAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Recado = models.TextField(blank=False, null=False)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="AgendaRecadoId"
    )

    class Meta:
        db_table = "AgendasRecados"
        verbose_name = "AgendaRecado"
        verbose_name_plural = "AgendasARecados"
        UniqueConstraint(fields=["AgendaRecadoId"], name="AgendaRecadoPK")

    def __str__(self):
        return str(self.AgendaRecadoId)

    def get_absolute_url(self):
        return reverse("AgendasRecados:AgendasRecados", kwargs={"slug": self.slug})
