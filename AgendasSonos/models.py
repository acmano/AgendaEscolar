from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class AgendasSonos(models.Model):
    AgendaSonoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaSonoId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasSonosAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Inicio = models.TimeField(blank=False, null=False)
    Fim = models.TimeField(blank=False, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="AgendaSonoId")

    class Meta:
        db_table = "AgendasSonos"
        verbose_name = "AgendaSono"
        verbose_name_plural = "AgendasASonos"
        UniqueConstraint(fields=["AgendaSonoId"], name="AgendaSonoPK")

    def __str__(self):
        return str(self.AgendaSonoId)

    def get_absolute_url(self):
        return reverse("AgendasSonos:AgendasSonos", kwargs={"slug": self.slug})
