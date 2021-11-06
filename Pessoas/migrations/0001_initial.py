# Generated by Django 3.2.9 on 2021-11-06 23:00

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('PessoaId', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='PessoaId')),
                ('Nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('Apelido', models.CharField(max_length=50, verbose_name='Apelido')),
                ('DataNascimento', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('CPF', models.DecimalField(decimal_places=0, max_digits=11, null=True, verbose_name='CPF')),
                ('RG', models.CharField(max_length=11, null=True, verbose_name='RG')),
                ('EMail', models.EmailField(max_length=254)),
                ('Senha', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='Nome', unique=True)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'db_table': 'pessoas',
                'ordering': ('Nome',),
            },
        ),
    ]