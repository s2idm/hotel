# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-15 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, verbose_name='Titre')),
                ('sousTitre', models.CharField(max_length=50, verbose_name='Sous titre')),
                ('image', models.ImageField(upload_to='carousel_uploads', verbose_name='image')),
                ('ordre', models.IntegerField(verbose_name='Ordre')),
                ('afficher', models.BooleanField(verbose_name='Afficher')),
            ],
        ),
        migrations.CreateModel(
            name='Gallerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=155, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesGallerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=155, verbose_name='Titre')),
                ('image', models.ImageField(upload_to='carousel_uploads', verbose_name='image')),
                ('ordre', models.IntegerField(verbose_name='Ordre')),
                ('afficher', models.BooleanField(verbose_name='Afficher')),
                ('gallerie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Gallerie')),
            ],
        ),
    ]
