from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.
class Alimentos(models.Model):
    AlimentoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AlimentoId",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="Nome")

    class Meta:
        db_table = "alimentos"
        ordering = ("Nome",)
        verbose_name = "Alimento"
        verbose_name_plural = "Alimentos"

    def __str__(self):
        return str(self.Nome)

    def get_absolute_url(self):
        return reverse("Alimentos:alimentos", kwargs={"slug": self.slug})
