from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.


class ResponsaveisALunos(models.Model):
    ResponsavelALunoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ResponsavelALunoId",
    )
    ResponsavelId = models.ForeignKey(
        "Responsaveis.Responsaveis",
        related_name="ResponsaveisAlunosResponsavel",
        verbose_name="Responsavel",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    AlunoId = models.ForeignKey(
        "Alunos.Alunos",
        related_name="ResponsaveisAlunosAluno",
        verbose_name="Aluno",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="ResponsavelALuno"
    )

    class Meta:
        db_table = "responsaveisalunos"
        verbose_name = "ResponsavelAluno"
        verbose_name_plural = "ResponsaveisALunos"

    def __str__(self):
        return str(self.AlunoId)

    def get_absolute_url(self):
        return reverse(
            "ResponsaveisALunos:responsaveisalunos", kwargs={"slug": self.slug}
        )
