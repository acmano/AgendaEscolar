from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.


class Responsaveis(models.Model):
    ResponsavelId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ResponsavelId",
    )
    PessoaId = models.ForeignKey(
        "Pessoas.Pessoas",
        related_name="ResponsaveisPessoas",
        verbose_name="Pessoa",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="ResponsavelId"
    )

    class Meta:
        db_table = "responsaveis"
        verbose_name = "Responsavel"
        verbose_name_plural = "Responsaveis"

    def __str__(self):
        return str(self.ResponsavelId)

    def get_absolute_url(self):
        return reverse("Responsaveis:responsaveis", kwargs={"slug": self.slug})
