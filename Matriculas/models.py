from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Matriculas(models.Model):
    MatriculaId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="MatriculaId",
    )
    TurmaId = models.ForeignKey(
        "Turmas.Turmas",
        related_name="MatriculasTurma",
        verbose_name="Turma",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    AlunoId = models.ForeignKey(
        "Alunos.Alunos",
        related_name="MatriculasAluno",
        verbose_name="Aluno",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="MatriculaId")

    class Meta:
        db_table = "Matriculas"
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"
        unique_together = ("TurmaId", "AlunoId")
        UniqueConstraint(fields=["MatriculaId"], name="MatriculasPK")
        UniqueConstraint(fields=["TurmaId", "AlunoId"], name="MatriculasAK")

    def __str__(self):
        return str(self.AlunoId)

    def get_absolute_url(self):
        return reverse("Matriculas:Matriculas", kwargs={"slug": self.slug})
