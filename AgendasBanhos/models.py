from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class AgendasBanhos(models.Model):
    AgendaBanhoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaBanhoId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasBanhosAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    Hora = models.TimeField(blank=False, null=False)
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="AgendaBanhoId"
    )

    class Meta:
        db_table = "AgendasBanhos"
        verbose_name = "AgendaBanho"
        verbose_name_plural = "AgendasABanhos"
        UniqueConstraint(fields=["AgendaBanhoId"], name="AgendaBanhoPK")

    def __str__(self):
        return str(self.AgendaBanhoId)

    def get_absolute_url(self):
        return reverse("AgendasBanhos:AgendasBanhos", kwargs={"slug": self.slug})
