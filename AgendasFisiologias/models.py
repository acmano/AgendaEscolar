from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Fisiologia(models.TextChoices):
    Fralda = "F", "Fralda"
    Unina = "U", "Urina"
    Fezes = "Z", "Fezes"
    Vomito = "V", "Vômito"


class AgendasFisiologias(models.Model):
    AgendaFisiologiaId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaFisiologiaId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasFisiologiasAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Hora = models.TimeField(verbose_name="Hora", blank=False, null=False)
    Tipo = models.CharField(max_length=1, choices=Fisiologia.choices)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="AgendaFisiologiaId"
    )

    class Meta:
        db_table = "AgendasFisiologias"
        verbose_name = "AgendaFisiologia"
        verbose_name_plural = "AgendasFisiologias"
        UniqueConstraint(fields=["AgendaFisiologiaId"], name="AgendaFisiologiaPK")

    def __str__(self):
        return str(self.AgendaFisiologiaId)

    def get_absolute_url(self):
        return reverse(
            "AgendasFisiologias:AgendasFisiologias", kwargs={"slug": self.slug}
        )
