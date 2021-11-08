from django.db import models
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.db import models

# Create your models here.


class Professores(models.Model):
    ProfessorId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ProfessorId",
    )
    PessoaId = models.ForeignKey(
        "Pessoas.Pessoas",
        related_name="ProfessoresPessoas",
        verbose_name="Pessoa",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="ProfessorId")

    class Meta:
        db_table = "professores"
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        UniqueConstraint(fields=["ProfessorId"], name="ProfessoresPK")
        UniqueConstraint(fields=["PessoaId"], name="ProfessoresAK")

    def __str__(self):
        return str(self.ProfessorId)

    def get_absolute_url(self):
        return reverse("Professore:professore", kwargs={"slug": self.slug})
