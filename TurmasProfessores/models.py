from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.


class TurmasProfessores(models.Model):
    TurmaProfessorId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="TurmaProfessorId",
    )
    TurmaId = models.ForeignKey(
        "Turmas.Turmas",
        related_name="TurmasProfessoresTurma",
        verbose_name="Turma",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    ProfessorId = models.ForeignKey(
        "Professores.Professores",
        related_name="TurmasProfessoresProfessor",
        verbose_name="Professor",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(
        unique=True, always_update=False, populate_from="TurmaProfessor"
    )

    class Meta:
        db_table = "TurmasProfessores"
        verbose_name = "TurmaProfessor"
        verbose_name_plural = "TurmasProfessores"

    def __str__(self):
        return str(self.ProfessorId)

    def get_absolute_url(self):
        return reverse(
            "TurmasProfessores:TurmasProfessores", kwargs={"slug": self.slug}
        )
