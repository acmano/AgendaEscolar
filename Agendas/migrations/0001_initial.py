# Generated by Django 3.2.9 on 2021-11-07 14:38

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TurmasProfessores', '0001_initial'),
        ('Matriculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendas',
            fields=[
                ('AgendaId', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='AgendaId')),
                ('Data', models.DateField(verbose_name='Data')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='AgendaId', unique=True)),
                ('MatriculaId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AgendasMatricula', to='Matriculas.matriculas', verbose_name='Matricula')),
                ('TurmaProfessorId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AgendasTurmaProfessor', to='TurmasProfessores.turmasprofessores', verbose_name='TurmaProfessor')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
                'db_table': 'Agendas',
                'unique_together': {('MatriculaId', 'TurmaProfessorId', 'Data')},
            },
        ),
    ]
