# Generated by Django 3.2.9 on 2021-11-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='AnoEscolar',
            field=models.IntegerField(verbose_name='Ano Escolar'),
        ),
    ]
