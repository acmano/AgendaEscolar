from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.
class Medicamentos(models.Model):
    MedicamentoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="MedicamentoId",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="Nome")

    class Meta:
        db_table = "medicamentos"
        ordering = ("Nome",)
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        UniqueConstraint(fields=["MedicamentoId"], name="MedicamentoPK")
        UniqueConstraint(fields=["Nome"], name="MedicamentoAK")

    def __str__(self):
        return str(self.Nome)

    def get_absolute_url(self):
        return reverse("Medicamentos:medicamentos", kwargs={"slug": self.slug})
