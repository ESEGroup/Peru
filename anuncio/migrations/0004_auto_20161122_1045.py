# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0003_auto_20161122_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidade',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncio.Localidade'),
        ),
    ]