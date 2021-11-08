from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Turmas(models.Model):
    TurmaId = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="TurmaId"
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome Da Turma", blank=False, null=False
    )
    AnoLetivo = models.IntegerField(verbose_name="Ano Letivo")
    AnoEscolar = models.IntegerField(verbose_name="Ano Escolar")
    slug = AutoSlugField(unique=True, always_update=False, populate_from="AnoLetivo")

    class Meta:
        db_table = "turmas"
        ordering = ("AnoLetivo",)
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        UniqueConstraint(fields=['TurmaId'], name='TurmasPK')
        UniqueConstraint(fields=['Nome'], name='TurmasAK')

    def __str__(self):
        return str(self.AnoLetivo)

    def get_absolute_url(self):
        return reverse("Turmas:turmas", kwargs={"slug": self.slug})
