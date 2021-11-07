from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Agendas(models.Model):
    AgendaId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AgendaId",
    )
    MatriculaId = models.ForeignKey(
        "Matriculas.Matriculas",
        related_name="AgendasMatricula",
        verbose_name="Matricula",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    TurmaProfessorId = models.ForeignKey(
        "TurmasProfessores.TurmasProfessores",
        related_name="AgendasTurmaProfessor",
        verbose_name="TurmaProfessor",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    Data = models.DateField(verbose_name="Data", blank=False, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="AgendaId")

    class Meta:
        db_table = "Agendas"
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        unique_together = ("MatriculaId", "TurmaProfessorId", "Data")
        UniqueConstraint(fields=["AgendaId"], name="AgendaPK")
        UniqueConstraint(
            fields=["MatriculaId", "TurmaProfessorId", "Data"], name="AgendaAK"
        )

    def __str__(self):
        return str(self.AgendaId)

    def get_absolute_url(self):
        return reverse("Agendas:Agendas", kwargs={"slug": self.slug})
