from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.


class Prescricoes(models.Model):
    PrescricaoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="PrescricaoId",
    )
    MedicamentoId = models.ForeignKey(
        "Medicamentos.Medicamentos",
        related_name="PrescricoesMedicamento",
        verbose_name="Medicamento",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    AlunoId = models.ForeignKey(
        "Alunos.Alunos",
        related_name="PrescricoesAluno",
        verbose_name="Aluno",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    DataInicio = models.DateField(
        verbose_name="Data de Início", blank=False, null=False
    )
    DataFim = models.DateField(verbose_name="Data Final", blank=False, null=False)
    Posologia = models.CharField(
        verbose_name="Posologia", max_length=50, blank=False, null=False
    )
    Horarios = models.CharField(
        verbose_name="Horários", max_length=50, blank=False, null=False
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="Prescricao")

    class Meta:
        db_table = "Prescricoes"
        verbose_name = "Prescricao"
        verbose_name_plural = "Prescricoes"

    def __str__(self):
        return str(self.AlunoId)

    def get_absolute_url(self):
        return reverse("Prescricoes:Prescricoes", kwargs={"slug": self.slug})
