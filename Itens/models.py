from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.
class Itens(models.Model):
    ItemId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ItemId",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="Nome")

    class Meta:
        db_table = "itens"
        ordering = ("Nome",)
        verbose_name = "Item"
        verbose_name_plural = "Itens"
        UniqueConstraint(fields=["ItemId"], name="ItensPK")
        UniqueConstraint(fields=["Nome"], name="NomeAK")

    def __str__(self):
        return str(self.Nome)

    def get_absolute_url(self):
        return reverse("Itens:itens", kwargs={"slug": self.slug})
