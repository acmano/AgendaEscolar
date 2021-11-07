from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# Create your models here.


class Alunos(models.Model):
    AlunoId = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="AlunoId",
    )
    PessoaId = models.ForeignKey(
        "Pessoas.Pessoas",
        related_name="AlunosPessoas",
        verbose_name="Pessoa",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="AlunoId")

    class Meta:
        db_table = "alunos"
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return str(self.AlunoId)

    def get_absolute_url(self):
        return reverse("Alunos:alunos", kwargs={"slug": self.slug})
