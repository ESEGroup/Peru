# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0004_auto_20161122_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='localidade',
            name='nome_filtro',
            field=models.CharField(default='notready', max_length=10),
            preserve_default=False,
        ),
    ]