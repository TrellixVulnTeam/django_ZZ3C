# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_autor_libro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='autor',
            new_name='nombre_autor',
        ),
    ]
