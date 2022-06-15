# Generated by Django 3.2.9 on 2022-06-14 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0006_auto_20220613_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmasTabelas',
            fields=[
                ('TurmaTabela_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='TurmaTabela_id')),
                ('Tabela', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.tabelasprecos')),
                ('Turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.turmas')),
            ],
            options={
                'verbose_name': 'Tabela de Preços da Turma',
                'verbose_name_plural': 'Tabelas de Preços das Turmas',
                'db_table': 'TurmasTabelas',
            },
        ),
    ]