# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180528_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='semestre',
            field=models.CharField(choices=[('semestre1', 'semestre1'), ('semestre2', 'semestre2')], default='semestre1', max_length=9),
        ),
    ]
