# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180602_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emploi_du_temp_enseignant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='emploi_du_temp_etudiant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='emploi_du_temp_examin_etudiant',
            name='image',
        ),
        migrations.AddField(
            model_name='emploi_du_temp_enseignant',
            name='Dimanche',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_enseignant',
            name='Jeudi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_enseignant',
            name='Lundi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_enseignant',
            name='Mardi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_enseignant',
            name='Mercredi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='Dimanche',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='Jeudi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='Lundi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='Mardi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_etudiant',
            name='Mercredi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_examin_etudiant',
            name='Dimanche',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_examin_etudiant',
            name='Jeudi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_examin_etudiant',
            name='Lundi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_examin_etudiant',
            name='Mardi',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='emploi_du_temp_examin_etudiant',
            name='Mercredi',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
