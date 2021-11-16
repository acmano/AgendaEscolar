from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.


class Aceite(models.TextChoices):
    Otimo = "O", "Ótimo"
    Regular = "R", "Regular"
    MAR = "G", "Rejeitou"


class Fisiologia(models.TextChoices):
    Fralda = "F", "Fralda"
    Unina = "U", "Urina"
    Fezes = "Z", "Fezes"
    Vomito = "V", "Vômito"


# Nivel 0 Alimentos
class Alimentos(models.Model):
    Alimento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Alimento_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return "{}".format(self.Nome)

    class Meta:
        db_table = "Alimentos"
        ordering = ("Nome",)
        verbose_name = "Alimento"
        UniqueConstraint(fields=["Alimento_id"], name="AlimentosPK")
        UniqueConstraint(fields=["Nome"], name="AlimentosAK")


# Nivel 0 Itens
class Itens(models.Model):
    Item_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Item_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return "{}".format(self.Nome)

    class Meta:
        db_table = "Itens"
        ordering = ("Nome",)
        verbose_name = "Item"
        UniqueConstraint(fields=["Item_id"], name="ItensPK")
        UniqueConstraint(fields=["Nome"], name="ItensAK")


# Nivel 0 Medicamentos
class Medicamentos(models.Model):
    Medicamento_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Medicamento_id",
    )
    Nome = models.CharField(
        max_length=50, verbose_name="Nome", blank=False, null=False, unique=True
    )
    Descricao = models.CharField(
        max_length=150,
        verbose_name="Descrição",
        blank=False,
        null=False,
    )

    def __str__(self):
        return "{}".format(self.Nome)

    class Meta:
        db_table = "Medicamentos"
        ordering = ("Nome",)
        verbose_name = "Medicamento"
        UniqueConstraint(fields=["Medicamento_id"], name="MedicamentosPK")
        UniqueConstraint(fields=["Nome"], name="MedicamentosAK")


# Nivel 0 Pessoas
class Pessoas(models.Model):
    Pessoa_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Pessoa_id"
    )
    Nome = models.CharField(
        max_length=50,
        verbose_name="Nome",
        blank=False,
        null=False,
        unique=True,
    )
    Apelido = models.CharField(
        max_length=50,
        verbose_name="Apelido",
        blank=False,
        null=False,
        unique=False,
    )
    DataNascimento = models.DateField(verbose_name="Data de Nascimento", null=True)
    CPF = models.DecimalField(
        verbose_name="CPF", max_digits=11, decimal_places=0, null=True
    )
    RG = models.CharField(verbose_name="RG", max_length=11, null=True)
    EMail = models.EmailField()
    Senha = models.CharField(max_length=150)

    def __str__(self):
        return "{} ({})".format(self.Apelido, self.Nome)

    class Meta:
        db_table = "Pessoas"
        ordering = ("Nome",)
        verbose_name = "Pessoa"
        UniqueConstraint(fields=["Pesoa_id"], name="PessoasAK")
        UniqueConstraint(fields=["Nome"], name="PessoasAK")


# Nivel 0 Turmas
class Turmas(models.Model):
    TurmaId = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="TurmaId"
    )
    Nome = models.CharField(
        max_length=50,
        verbose_name="Nome",
        blank=False,
        null=False,
        unique=True,
    )
    AnoLetivo = models.IntegerField(verbose_name="Ano Letivo")
    AnoEscolar = models.IntegerField(verbose_name="Ano Escolar")

    def __str__(self):
        return "{}".format(self.Nome)

    class Meta:
        db_table = "Turmas"
        ordering = ("AnoLetivo", "AnoEscolar")
        verbose_name = "Turma"
        UniqueConstraint(fields=["TurmaId"], name="TurmasPK")
        UniqueConstraint(fields=["Nome"], name="TurmasAK")


# Nivel 1 Alunos
class Alunos(models.Model):
    Aluno_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Aluno_id"
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.Pessoa.Nome)

    class Meta:
        db_table = "Alunos"
        verbose_name = "Aluno"
        UniqueConstraint(fields=["Aluno_id"], name="AlunosPK")
        UniqueConstraint(fields=["Pessoa"], name="AlunosAK")


# Nivel 1 Professores
class Professores(models.Model):
    Professor_id = models.AutoField(
        auto_created=True, primary_key=True, serialize=True, verbose_name="Professor_id"
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.Pessoa.Nome)

    class Meta:
        db_table = "Professores"
        verbose_name = "Professor"
        UniqueConstraint(fields=["Professor_id"], name="ProfessorPK")
        UniqueConstraint(fields=["Pessoa"], name="ProfessorAK")


# Nivel 1 Responsaveis
class Responsaveis(models.Model):
    Responsavel_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="Responsavel_id",
    )
    Pessoa = models.OneToOneField(Pessoas, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.Pessoa.Nome)

    class Meta:
        db_table = "Responsaveis"
        verbose_name = "Responsavel"
        UniqueConstraint(fields=["Responsavel_id"], name="ResponsavelPK")
        UniqueConstraint(fields=["Pessoa"], name="ResponsavelAK")


# Nivel 2 ResponsaveisAlunos
class ResponsaveisAlunos(models.Model):
    ResponsavelAluno_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=True,
        verbose_name="ResponsavelAluno_id",
    )
    Responsavel = models.ForeignKey(
        Responsaveis, db_index=True, on_delete=models.PROTECT
    )
    Aluno = models.ForeignKey(Alunos, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{}:{}".format(self.Responsavel.Pessoa.Nome, self.Aluno.Pessoa.Nome)

    class Meta:
        db_table = "ResponsaveisAlunos"
        verbose_name = "ResponsavelAluno"
        UniqueConstraint(fields=["ResponsavelAluno_id"], name="ResponsavelAlunoPK")
