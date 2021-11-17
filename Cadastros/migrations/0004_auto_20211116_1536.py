# Generated by Django 3.2.9 on 2021-11-16 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0003_alter_alunos_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='Pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.pessoas'),
        ),
        migrations.AlterField(
            model_name='professores',
            name='Pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Cadastros.pessoas'),
        ),
    ]