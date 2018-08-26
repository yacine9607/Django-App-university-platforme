# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_matière_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='document_chefDepartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='document_chef/')),
                ('chef_departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Chef_Departement')),
            ],
        ),
        migrations.CreateModel(
            name='document_filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='document_filiere/')),
                ('responsable_filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Responsable_Filière')),
            ],
        ),
        migrations.CreateModel(
            name='document_PG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='document_PG/')),
                ('responsable_pg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Adjoint_PG')),
            ],
        ),
        migrations.CreateModel(
            name='document_scolarite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='document_filiere/')),
                ('adjoint_scolarite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Adjoint_scolarité')),
            ],
        ),
        migrations.AlterField(
            model_name='parcour',
            name='nom',
            field=models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2'), ('Doctorant', 'Doctorant')], max_length=10),
        ),
    ]