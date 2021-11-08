# Generated by Django 3.2.9 on 2021-11-07 13:24

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('ItemId', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ItemId')),
                ('Nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='Nome', unique=True)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'db_table': 'itens',
                'ordering': ('Nome',),
            },
        ),
    ]