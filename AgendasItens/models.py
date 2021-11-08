from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class AgendasItens(models.Model):
    AgendaItemId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaItemId",
    )
    AgendaId = models.ForeignKey(
        "Agendas.Agendas",
        related_name="AgendasItensAgendas",
        verbose_name="Agenda",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    ItemId = models.ForeignKey(
        "Itens.Itens",
        related_name="AgendasItensItens",
        verbose_name="Item",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataHora = models.DateTimeField(verbose_name="DataHora", auto_now_add=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="AgendaItemId")

    class Meta:
        db_table = "AgendasItens"
        verbose_name = "AgendaItem"
        verbose_name_plural = "AgendasAItens"
        unique_together = ("AgendaId", "ItemId")
        UniqueConstraint(fields=["AgendaItemId"], name="AgendaItemPK")
        UniqueConstraint(fields=["AgendaId", "PrescricaoId"], name="AgendaItemAK")

    def __str__(self):
        return str(self.AgendaItemId)

    def get_absolute_url(self):
        return reverse("AgendasItens:AgendasItens", kwargs={"slug": self.slug})
