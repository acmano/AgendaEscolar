from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Aceite(models.TextChoices):
    Otimo = "O", "Ótimo"
    Regular = "R", "Regular"
    MAR = "G", "Rejeitou"


class AgendasAlimentos(models.Model):
    AgendaAlimentoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaAlimentoId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasAlimentosAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    AlimentoId = models.ForeignKey(
        "Alimentos.Alimentos",
        related_name="AgendasAlimentosAlimentos",
        verbose_name="Alimento",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Hora = models.TimeField(verbose_name="Hora", blank=False, null=False)
    Aceite = models.CharField(max_length=1, choices=Aceite.choices)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="AgendaAlimentoId"
    )

    class Meta:
        db_table = "AgendasAlimentos"
        verbose_name = "AgendaAlimento"
        verbose_name_plural = "AgendasAlimentos"
        unique_together = ("AgendaId", "AlimentoId", "Hora")
        UniqueConstraint(fields=["AgendaAlimentoId"], name="AgendaAlimentoPK")
        UniqueConstraint(fields=["AgendaId", "AlimentoId", "Hora"], name="AgendaAK")

    def __str__(self):
        return str(self.AgendaAlimentoId)

    def get_absolute_url(self):
        return reverse("AgendasAlimentos:AgendasAlimentos", kwargs={"slug": self.slug})
