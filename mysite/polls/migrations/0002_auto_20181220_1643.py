# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-20 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='chocie_text',
            new_name='choice_text',
        ),
    ]
