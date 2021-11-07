# Generated by Django 3.2.9 on 2021-11-07 13:35

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Responsaveis', '0002_alter_responsaveis_pessoaid'),
        ('Alunos', '0002_alter_alunos_pessoaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsaveisALunos',
            fields=[
                ('ResponsavelALunoId', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ResponsavelALunoId')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='ResponsavelALuno', unique=True)),
                ('AlunoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ResponsaveisAlunosAluno', to='Alunos.alunos', verbose_name='Aluno')),
                ('ResponsavelId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ResponsaveisAlunosResponsavel', to='Responsaveis.responsaveis', verbose_name='Responsavel')),
            ],
            options={
                'verbose_name': 'ResponsavelAluno',
                'verbose_name_plural': 'ResponsaveisALunos',
                'db_table': 'responsaveisalunos',
            },
        ),
    ]
