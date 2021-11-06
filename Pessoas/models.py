from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

# from .models import users

# Create your models here.


class Pessoas(models.Model):
    PessoaId = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="PessoaId"
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Apelido = models.CharField(
        max_length=50, verbose_name="Apelido", blank=False, null=False
    )
    DataNascimento = models.DateField(verbose_name="Data de Nascimento", null=True)
    CPF = models.DecimalField(
        verbose_name="CPF", max_digits=11, decimal_places=0, null=True
    )
    RG = models.CharField(verbose_name="RG", max_length=11, null=True)
    EMail = models.EmailField()
    Senha = models.CharField(max_length=150)
    #    UserId = models.ForeignKey(
    #        "users.id",
    #        related_name="users",
    #        blank=True,
    #        null=True,
    #        on_delete=models.PROTECT,
    #    )
    slug = AutoSlugField(unique=True, always_update=False, populate_from="Nome")

    class Meta:
        db_table = "pessoas"
        ordering = ("Nome",)
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return str(self.Nome)

    def get_absolute_url(self):
        return reverse("Pessoas:pessoas", kwargs={"slug": self.slug})
